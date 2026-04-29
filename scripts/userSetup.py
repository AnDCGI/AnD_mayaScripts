# Licensed under the MIT license

"""Bootstrap the AnD CGI shelf when Maya starts."""

from __future__ import annotations

import maya.cmds as cmds
import maya.mel as mel

from AnD_mayaCommon import REPO_ROOT, SHELF_FILE, add_icon_path, add_py_script_paths


def load():
    """Load the AnDCGI shelf after Maya has finished initializing."""
    if cmds.about(batch=True):
        return

    add_py_script_paths()
    add_icon_path()

    if not SHELF_FILE.is_file():
        cmds.warning(
            "AnD Maya shelf was not found: {}. Set AND_MAYA_REPO_ROOT to the "
            "AnD_mayaScripts checkout if Maya cannot auto-detect it.".format(SHELF_FILE)
        )
        return

    shelf_name = SHELF_FILE.stem.replace("shelf_", "")
    if cmds.shelfLayout(shelf_name, exists=True):
        cmds.deleteUI(shelf_name)

    mel.eval('loadNewShelf("{}")'.format(str(SHELF_FILE).replace("\\", "/")))
    print("Loaded AnDCGI shelf from {}".format(REPO_ROOT))


cmds.evalDeferred(load)
