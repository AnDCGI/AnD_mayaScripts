#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2021 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

import maya.cmds as cmds      # Importing The Main Maya Python Module

# Declareing The Default Name Spaces
defaults = ['UI', 'shared']

# Set To :(root) Name Space
cmds.namespace(setNamespace=':')

# Used As A Sort Key, This Will Sort Namespaces By How Many Children They Have.
def numChildren(nmSp):
    return nmSp.count(':')

# Get The List Of All Name Spaces In The Scene Excuding Defaults
nameSpaces = [nmSp for nmSp in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True) if nmSp not in defaults]

# Reverse The List, So Name Spaces With More Children Comes On First.
nameSpaces.sort(key=numChildren, reverse=True) # Skip This Line If Need To Delete One By One

# Looping Over All To Remove
for name in nameSpaces:
    print(name)
    cmds.namespace( removeNamespace = name, mergeNamespaceWithRoot = True, force=True) # Name Spaces Must Be Empty For Removal
