#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

"""Delete Arnold AOV nodes after importing scene references."""

import maya.cmds as cmds

# Import references first because some AOV nodes can live inside them.
refs = cmds.ls(type="reference") or []
for ref in refs:
    if ref in ("sharedReferenceNode", "_UNKNOWN_REF_NODE_"):
        continue
    try:
        rFile = cmds.referenceQuery(ref, filename=True)
        cmds.file(rFile, importReference=True)
    except RuntimeError as error:
        cmds.warning("Could not import reference {}: {}".format(ref, error))

# Delete every Arnold AOV node that remains in the current scene.
aovList = cmds.ls(type="aiAOV") or []
for node in aovList:
    print(node + " has been removed")
    cmds.delete(node)
