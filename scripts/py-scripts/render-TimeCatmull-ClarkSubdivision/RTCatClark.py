#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

'''A Render-Time Catmull-Clark Subdivision Script for Maya
Tested with Maya Software, Maya Hardware, Arnold, V-Ray.
It should work with practically any render engines inside Maya that supports the
Pre & Post Render Scripts
This scripts subdivides any mesh at render time that has Smooth Mesh Preview 3
& reverts it back to previous state after render is fished.
In order for this script to work add this
Pre Render MEL = python("import RTCatClark;RTCatClark.preCatClark()")
Post Render MEL = python("import RTCatClark;RTCatClark.pstCatClark()")
Be sure to add the "__init__.py" inside the Maya script directory
Also mention the PYTHONPATH in Maya environment  where the scripts is stored.
'''

import maya.cmds as cmds    # Importing The Main Maya Python Module


def preCatClark():
    # This Subdivides Every Polygon Objetcs In Scene Equals To 3 Smooth In Maya
    objects = cmds.ls(type='mesh')

    if objects:
        for shapes in objects:
            smoothState = cmds.displaySmoothness(
                shapes, q=True, polygonObject=True)
            if smoothState:
                if smoothState[0] == 3:
                    cmds.displaySmoothness(shapes, polygonObject=1)
                    smoothShapes = cmds.polySmooth(shapes, ch=True, dv=2)
                    cmds.rename(smoothShapes, 'pRCatClark_' + shapes)


def pstCatClark():
    # This Chnages Subdivision States Back To Normal Equals To 1 Smooth In Maya
    smoothShapes = cmds.ls(type='polySmoothFace')

    if smoothShapes:
        for prim in smoothShapes:
            if prim[:10] == 'pRCatClark':
                shapes = cmds.listConnections(prim + '.output')
                cmds.polySmooth(prim, e=True, dv=0)
                cmds.delete(prim)
                cmds.displaySmoothness(shapes, polygonObject=3)
                cmds.select(clear=True)
