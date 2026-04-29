"""Copy and paste selected Maya channel values between objects.

The copied values are written to the system temp directory so separate Maya
sessions can share the same clipboard file.
"""

from __future__ import annotations

import pickle

import maya.cmds as cmds

from AnD_mayaCommon import temp_state_file


CLIPBOARD_PATH = temp_state_file("and_maya_channel_clipboard.pkl")


def _selected_channels():
    xform_channels = cmds.channelBox("mainChannelBox", query=True, sma=True) or []
    shape_channels = cmds.channelBox("mainChannelBox", query=True, ssa=True) or []
    shape_objects = cmds.channelBox("mainChannelBox", query=True, sol=True) or []
    return xform_channels, shape_channels, shape_objects


def copyChan():
    """Copy highlighted channel box values from the first selected object."""
    selection = cmds.ls(selection=True) or []
    if not selection:
        cmds.error("Select an object before copying channels.")
        return

    obj = selection[0]
    xform_channels, shape_channels, shape_objects = _selected_channels()
    xform_values = {}
    shape_values = {}

    for attr in xform_channels:
        xform_values[attr] = cmds.getAttr("{}.{}".format(obj, attr))

    if shape_channels and shape_objects:
        source_shape = shape_objects[0]
        for attr in shape_channels:
            shape_values[attr] = cmds.getAttr("{}.{}".format(source_shape, attr))

    with CLIPBOARD_PATH.open("wb") as handle:
        pickle.dump([xform_values, shape_values], handle, protocol=pickle.HIGHEST_PROTOCOL)

    cmds.inViewMessage(
        amg="Selected channels copied",
        pos="botCenter",
        fade=True,
    )


def pasteChan():
    """Paste copied channel values onto every selected object."""
    objects = cmds.ls(selection=True) or []
    if not objects:
        cmds.error("Select one or more objects before pasting channels.")
        return

    if not CLIPBOARD_PATH.exists():
        cmds.error("No copied channel data found. Run copy first.")
        return

    with CLIPBOARD_PATH.open("rb") as handle:
        xform_values, shape_values = pickle.load(handle)

    for attr, value in xform_values.items():
        for obj in objects:
            try:
                cmds.setAttr("{}.{}".format(obj, attr), value)
            except RuntimeError:
                pass

    all_shapes = list(objects)
    for obj in objects:
        shapes = cmds.listRelatives(obj, shapes=True) or []
        all_shapes.extend(shapes)

    for attr, value in shape_values.items():
        for shape in all_shapes:
            try:
                cmds.setAttr("{}.{}".format(shape, attr), value)
            except RuntimeError:
                pass

    cmds.inViewMessage(
        amg="Channels pasted to <hl>{}</hl> object(s)".format(len(objects)),
        pos="botCenter",
        fade=True,
    )
