#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Save the current scene with simple automatic versioning.

Optional configuration keys in ``~/Documents/AnD_mayaScripts/config.json``:

``save_scene_root``
    Root directory where versioned scenes are saved. Defaults to the current
    workspace's ``scenes`` directory.
``save_scene_prefix``
    Prefix used for new scene names. Defaults to the current scene/camera name.
"""

from __future__ import annotations

import re
from pathlib import Path

import maya.cmds as cmds

from AnD_mayaCommon import config_value, ensure_directory


VERSION_PATTERN = re.compile(r"_v(\d{3})\.ma$", re.IGNORECASE)


def _safe_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_]+", "_", value.strip())
    return value.strip("_") or "maya_scene"


def _default_name() -> str:
    scene_name = cmds.file(query=True, sceneName=True)
    if scene_name:
        return _safe_name(Path(scene_name).stem)

    cameras = [cam for cam in (cmds.listCameras(perspective=True) or []) if cam != "persp"]
    if cameras:
        return _safe_name(cameras[0])

    return "maya_scene"


def _next_version_path(directory: Path, prefix: str) -> Path:
    versions = []
    for path in directory.glob("{}_v*.ma".format(prefix)):
        match = VERSION_PATTERN.search(path.name)
        if match:
            versions.append(int(match.group(1)))
    version = max(versions, default=0) + 1
    return directory / "{}_v{:03d}.ma".format(prefix, version)


def save_versioned_scene():
    workspace_root = cmds.workspace(query=True, rootDirectory=True)
    default_root = Path(workspace_root) / "scenes" if workspace_root else Path.home() / "maya" / "scenes"
    save_root = ensure_directory(config_value("save_scene_root", str(default_root)))
    prefix = _safe_name(config_value("save_scene_prefix", _default_name()))
    target_path = _next_version_path(save_root, prefix)

    cmds.file(rename=str(target_path))
    cmds.file(save=True, type="mayaAscii")
    cmds.inViewMessage(
        amg="Saved scene as <hl>{}</hl>".format(target_path.name),
        pos="midCenter",
        fade=True,
    )


save_versioned_scene()
