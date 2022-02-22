#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

import maya.cmds as cmds    # Importing The Main Maya Python Module

# Importing All Reference, Without AOVs Can't Be Deleted
refs = cmds.ls(type="reference")
for i in refs:
    # These Two Lines Imports All References
    rFile = cmds.referenceQuery(i, f=True)
    cmds.file(rFile, importReference=True)
    # Getiing All AOVs In The Scene
    aovList = cmds.ls(type="aiAOV")
    # This Loops Deletes All AOVs
    for node in aovList:
        print(node+" has been removed")
        cmds.delete(node)
