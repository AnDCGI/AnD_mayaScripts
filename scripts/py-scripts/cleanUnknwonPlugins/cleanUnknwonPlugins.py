#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
Clean Unknown Plugins. This script will delete any unknown plugins from Maya Scene. The list of deleted plugins can 
be seen on Maya Script Editor
"""
import maya.cmds as cmds  # Importing The Main Maya Python Module

cmds.delete(cmds.ls(type="unknown"))
plg_ls = cmds.unknownPlugin(q=True, l=True)
if plg_ls:
    for plugin in plg_ls:
        print(plugin)
        cmds.unknownPlugin(plugin, r=True)
"""
When a pre-Maya 6.5 file that contains references is converted to a later version Maya file, a reference node named 
"_UNKNOWN_REF_NODE_" may be created and/or a special "_UNKNOWN_REF_NODE_" entry may be added to existing reference 
nodes. This node type was used to store any edits that were made prior to 6.5 until those edits could be applied. Once 
all references in the scene have been loaded, all edits should be applied and the _UNKNOWN_REF_NODE_ areas and nodes 
should disappear. If there are any edits which can not be applied (for example, nodes in the original reference file 
that were renamed or deleted), the _UNKNOWN_REF_NODE_ will remain in the file.

If you need to remove these reference nodes, you can do so by querying for the _UNKNOWN_REF_NODE_ and deleting it. 
That is, this specific node type cannot be deleted using the Reference Editor. In the Script Editor:

delete “_UNKNOWN_REF_NODE_”
"""
# Use The Bottom Line Only If You Have "_UNKNOWN_REF_NODE_"
if '_UNKNOWN_REF_NODE_' in cmds.ls(type='reference'):
    cmds.delete("_UNKNOWN_REF_NODE_")
