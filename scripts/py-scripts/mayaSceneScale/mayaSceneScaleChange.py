#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Â© 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
Maya one click Scene Scale Change. This script is designed to change scene scale
like for FX, Lighting etc. Designed to work as a shelf button inside Maya and
especially made to work with Alembic files.

Disclaimer! Be carefull while using it with Rigged Files.
"""

import maya.cmds as cmds
import maya.mel as mel


def scale_scene():
    """Wrap the scene in a single global scale locator."""
    # Turn inheritTransform back on for Alembic parents before scaling the scene.
    cmds.select(all=True, hierarchy=True)
    selection = cmds.ls(type='AlembicNode')
    transformNode = cmds.listRelatives(selection, parent=True) if selection else []

    if transformNode:
        for obj in transformNode:
            cmds.setAttr(obj + ".inheritsTransform", 1)
    cmds.select(clear=True)

    # Collect top-level assemblies so the scale control only wraps the scene once.
    cmds.select(all=True, noExpand=True)
    selection = cmds.ls(selection=True, assemblies=True)
    if not selection:
        cmds.select(clear=True)
        cmds.error("No scene assemblies found to scale.")
        return

    # Create a single locator that drives a global scale attribute.
    locator = cmds.spaceLocator(name='sceneScale')[0]
    cmds.parent(selection, locator)
    cmds.select(locator)
    cmds.addAttr(shortName='gs', longName='globalScale', defaultValue=0.1, minValue=0.01, maxValue=100, keyable=True)

    # Wire the custom attribute into the locator's scale channels.
    cmds.connectAttr(locator + '.gs', locator + '.scaleX')
    cmds.connectAttr(locator + '.gs', locator + '.scaleY')
    cmds.connectAttr(locator + '.gs', locator + '.scaleZ')

    # Give the locator a consistent outliner and viewport color.
    cmds.setAttr(locator + ".useOutlinerColor", 1)
    cmds.setAttr(locator + ".outlinerColor", 0, 1, 0)
    cmds.setAttr(locator + ".overrideEnabled", 1)
    cmds.setAttr(locator + ".overrideColor", 13)

    # Hide every transform channel except visibility and globalScale.
    selected = cmds.ls(selection=True)
    for eachTrn in selected:
        for tranAttrs in cmds.listAttr(eachTrn, keyable=True) or []:
            if tranAttrs not in ('visibility', 'globalScale'):
                cmds.setAttr(eachTrn + '.' + tranAttrs, keyable=False, cb=False, lock=True)

    # Hide local shape attributes so the control reads as a single-purpose tool.
    for eachShp in selected:
        for shp in cmds.listRelatives(eachShp, shapes=True) or []:
            for shpAtrs in cmds.listAttr(shp, string='local*') or []:
                cmds.setAttr(shp + '.' + shpAtrs, keyable=False, cb=False, lock=True)

    # Refresh Maya UI panels so the new locator state is visible immediately.
    mel.eval('AEdagNodeCommonRefreshOutliners()')
    mel.eval('AttributeEditor;updateAE("{}")'.format(locator))
    cmds.select(clear=True)

    cmds.inViewMessage(amg='New Scene Scale <hl>0.1</hl>', pos='midCenter', font="Cascadia Mono SemiBold", fade=True)
