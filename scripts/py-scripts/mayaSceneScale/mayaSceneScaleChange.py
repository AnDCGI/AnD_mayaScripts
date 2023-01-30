#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
Maya one click Scene Scale Change. This script is designed to change scene scale like for FX, Lighting etc. Designed to 
work as a shelf button inside Maya and especially made to work with Alembic files. By default it will scale everything 
down to 0.1 in all axis, User can later change the scale at any point. This is a headless script so watch out for in 
view message.

Disclaimer! Be carefull while using it with Rigged Files.
"""

import maya.cmds as cmds  # Importing The Main Maya Python Module
import maya.mel as mel  # Importing The Mel Python Wrapper Module

# Selecting Every ALembic Inside Scene Then Getting Transform Node
cmds.select(all=True, hierarchy=True)
selection = cmds.ls(type='AlembicNode')
transformNode = cmds.listRelatives(selection, p=True)

if transformNode:  # Check TransformNode If Any
    for obj in transformNode:  # Setting Inherit Transform On For Alembic Files
        cmds.setAttr(obj + ".inheritsTransform", 1)
cmds.select(clear=True)

cmds.select(all=True, noExpand=True)  # Selecting Everything Inside Scene Again
selection = cmds.ls(selection=True, assemblies=True)

# Creating Locator, Renaming & Making It Parent Of Everything Inside Scene
locator = cmds.spaceLocator()
cmds.parent(selection, locator)
cmds.select(locator)
cmds.rename(locator, 'sceneScale')
cmds.addAttr(shortName='gs', longName='globalScale', defaultValue=0.1, minValue=0.01, maxValue=100, keyable=True)

# Connecting To Global Scale
cmds.connectAttr('sceneScale.gs', 'sceneScale.scaleX')
cmds.connectAttr('sceneScale.gs', 'sceneScale.scaleY')
cmds.connectAttr('sceneScale.gs', 'sceneScale.scaleZ')

# Some Beautification Of The Locator So It Stands Out
cmds.setAttr("sceneScale.useOutlinerColor", 1)
cmds.setAttr("sceneScale" + ".outlinerColor", 0, 1, 0)
cmds.setAttr("sceneScale.overrideEnabled", 1)
cmds.setAttr("sceneScale" + ".overrideColor", 13)

# Lock & Hide Transform Attributes
selected = cmds.ls(selection=True)
for eachTrn in selected:
    for tranAttrs in cmds.listAttr(k=True):
        if tranAttrs == 'visibility' or tranAttrs == 'globalScale':
            pass
        else:
            cmds.setAttr(eachTrn + '.' + tranAttrs, keyable=False, cb=False, lock=True)

# Lock & Hide Shape Attributes
for eachShp in selected:
    for shp in cmds.listRelatives(selected, s=True):
        for shpAtrs in cmds.listAttr(shp, st='local*'):
            cmds.setAttr(shp + '.' + shpAtrs, keyable=False, cb=False, lock=True)

# Refreshing Outliner & Attribute Editor So That It Can Reflects The Change
mel.eval('AEdagNodeCommonRefreshOutliners()')
mel.eval('AttributeEditor;updateAE("sceneScale")')
cmds.select(clear=True)  # Clear Selection

# Message
cmds.inViewMessage(amg='New Scene Scale <hl>0.1</hl>', pos='midCenter', font="Cascadia Mono SemiBold", fade=True)
