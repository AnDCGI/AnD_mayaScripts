#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

import maya.cmds as cmds  # Importing The Main Maya Python Module

# *Selecting Mesh, Nurbs Surfaces & Subdivition Surfaces Only, Not Everything
# In The Scene.
sel = cmds.ls(ni=1, typ=["mesh", "nurbsSurface", "subdiv"])
num = len(sel)
for i in range(0, num):  # For Loop On Selection
    # Sets On Or Off Status
    selAttr = sel[i] + ".aiMatte"
    cmds.setAttr(selAttr, 1)
