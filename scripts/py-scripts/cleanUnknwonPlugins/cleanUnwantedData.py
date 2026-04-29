#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2026 AnD CGI. This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""Clean unwanted Maya scene data from one small UI."""

import maya.cmds as cmds

VERSION = '1.1.0'
WINDOW_ID = 'FileSanitation'
DEFAULT_NAMESPACES = {'UI', 'shared'}


def clean_namespaces():
    """Merge non-default namespaces into root."""
    cmds.namespace(setNamespace=':')
    namespaces = cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True) or []
    namespaces = [nmsp for nmsp in namespaces if nmsp not in DEFAULT_NAMESPACES]
    namespaces.sort(key=lambda nmsp: nmsp.count(':'), reverse=True)

    removed = []
    for namespace in namespaces:
        cmds.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=True, force=True)
        removed.append(namespace)
        print('Merged namespace: {}'.format(namespace))
    return removed


def clean_unknown_data():
    """Delete unknown nodes, unknown plugins, and legacy unknown ref nodes."""
    removed_nodes = cmds.ls(type='unknown') or []
    if removed_nodes:
        cmds.delete(removed_nodes)
        for node in removed_nodes:
            print('Deleted unknown node: {}'.format(node))

    removed_plugins = []
    for plugin in cmds.unknownPlugin(query=True, list=True) or []:
        cmds.unknownPlugin(plugin, remove=True)
        removed_plugins.append(plugin)
        print('Removed unknown plugin: {}'.format(plugin))

    removed_unknown_ref = False
    if '_UNKNOWN_REF_NODE_' in (cmds.ls(type='reference') or []):
        cmds.delete('_UNKNOWN_REF_NODE_')
        removed_unknown_ref = True
        print('Deleted _UNKNOWN_REF_NODE_')

    return removed_nodes, removed_plugins, removed_unknown_ref


def CreateButtonPush(*args):
    clean_namespaces_enabled = cmds.checkBoxGrp('cleanDataOptions', query=True, value1=True)
    clean_unknown_enabled = cmds.checkBoxGrp('cleanDataOptions', query=True, value2=True)

    if not clean_namespaces_enabled and not clean_unknown_enabled:
        cmds.warning('Select at least one cleanup option.')
        cmds.inViewMessage(amg='Select at least one cleanup option', pos='midCenter', fade=True)
        return

    summary = []

    if clean_namespaces_enabled:
        removed_namespaces = clean_namespaces()
        summary.append('Namespaces: {}'.format(len(removed_namespaces)))

    if clean_unknown_enabled:
        removed_nodes, removed_plugins, removed_unknown_ref = clean_unknown_data()
        summary.append('Unknown Nodes: {}'.format(len(removed_nodes)))
        summary.append('Unknown Plugins: {}'.format(len(removed_plugins)))
        if removed_unknown_ref:
            summary.append('Unknown Ref Node: 1')

    cmds.inViewMessage(
        amg='Cleanup complete <hl>{}</hl>'.format(' | '.join(summary)),
        pos='midCenter',
        fade=True,
    )


def DoneButtonPush(*args):
    if cmds.window(WINDOW_ID, exists=True):
        cmds.deleteUI(WINDOW_ID, window=True)


if cmds.window(WINDOW_ID, exists=True):
    cmds.deleteUI(WINDOW_ID, window=True)

window = cmds.window(
    WINDOW_ID,
    title='Scene Sanitization | v{}'.format(VERSION),
    resizeToFitChildren=True,
    sizeable=False,
    tlb=True,
)

cmds.frameLayout(label='Clean Unwanted Data', collapsable=False, mw=5, mh=5)
cmds.text(label='AnD CGI CC BY-SA 4.0', font='smallPlainLabelFont')
cmds.columnLayout(adjustableColumn=True)
cmds.checkBoxGrp(
    'cleanDataOptions',
    numberOfCheckBoxes=2,
    labelArray2=['Namespace', 'Unknown Plugins'],
    value1=True,
    value2=True,
)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(115, 115), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
cmds.button(label='Clean', command=CreateButtonPush)
cmds.button(label='Done', command=DoneButtonPush)
cmds.setParent('..')
cmds.showWindow(window)
