#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the current Maya scene to a daily batch render script.

Optional configuration keys in ``~/Documents/AnD_mayaScripts/config.json``:

``batch_render_output_dir``
    Directory where the generated ``.bat`` files are written.
``batch_render_frames_dir``
    Override render output directory passed to ``Render.exe -rd``.
``render_executable``
    Full path to ``Render.exe``. Defaults to ``Render`` on PATH.
"""

from __future__ import annotations

import getpass
from pathlib import Path

import maya.cmds as cmds

from AnD_mayaCommon import config_value, ensure_directory, maya_user_dir


def _quoted(path) -> str:
    return '"{}"'.format(str(path).replace("/", "\\"))


def _batch_file_path() -> Path:
    output_dir = config_value("batch_render_output_dir", str(maya_user_dir() / "batch_render"))
    output_dir = ensure_directory(output_dir)
    user = getpass.getuser().upper()
    user_tag = (user[0:1] + user[-1:]) if user else "AN"
    file_name = "{}_{}.bat".format(cmds.date(format="DD-MM-YYYY"), user_tag)
    return output_dir / file_name


def _render_output_dir(scene_path: Path) -> str:
    configured = config_value("batch_render_frames_dir")
    if configured:
        return _quoted(configured)
    return _quoted(scene_path.parent / "render")


def add_current_scene_to_batch():
    scene_name = cmds.file(query=True, sceneName=True)
    if not scene_name:
        cmds.error("Save the current scene before adding it to a batch render.")
        return

    scene_path = Path(scene_name)
    render_executable = config_value("render_executable", "Render")
    command = "{} -r file -rd {} {}".format(
        _quoted(render_executable),
        _render_output_dir(scene_path),
        _quoted(scene_path),
    )

    batch_path = _batch_file_path()
    with batch_path.open("a", encoding="utf-8") as handle:
        handle.write(command + "\n")

    cmds.inViewMessage(
        amg="Added scene to batch render script",
        pos="midCenter",
        fade=True,
    )
    print("Batch render command appended to {}".format(batch_path))
