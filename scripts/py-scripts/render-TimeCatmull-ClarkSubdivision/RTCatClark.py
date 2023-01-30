#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
A render-time catmull-clark subdivision script for Maya. Tested with Maya Software, Maya Hardware, Arnold, and V-Ray. 
It should work with practically any render engine inside Maya that supports the Pre & Post render scripts This script 
subdivides any mesh at render time that has smooth mesh preview 3 & reverts it back to the previous state after the 
render is fished. In order for this script to work add this in Render Settings >> Common >> Render Options >>

Pre Render MEL = python("import RTCatClark;RTCatClark.preCatClark()")
Post Render MEL = python("import RTCatClark;RTCatClark.pstCatClark()")

Be sure to add the "__init__.Py" inside the Maya script directory. Also mention the PYTHONPATH in the Maya environment 
where the scripts are stored.
"""

import maya.cmds as cmds  # Importing The Main Maya Python Module


def preCatClark():
    """This subdivides every polygon object in the scene equals 3 smooth in Maya."""
    objects = cmds.ls(type='mesh')

    if objects:
        for shapes in objects:
            smoothState = cmds.displaySmoothness(shapes, q=True, polygonObject=True)
            if smoothState:
                if smoothState[0] == 3:
                    cmds.displaySmoothness(shapes, polygonObject=1)
                    smoothShapes = cmds.polySmooth(shapes, ch=True, dv=2)
                    cmds.rename(smoothShapes, 'pRCatClark_' + shapes)


def pstCatClark():
    """This changes subdivision states back to normal equals 1 smooth in Maya."""
    smoothShapes = cmds.ls(type='polySmoothFace')

    if smoothShapes:
        for prim in smoothShapes:
            if prim[:10] == 'pRCatClark':
                shapes = cmds.listConnections(prim + '.output')
                cmds.polySmooth(prim, e=True, dv=0)
                cmds.delete(prim)
                cmds.displaySmoothness(shapes, polygonObject=3)
                cmds.select(clear=True)
