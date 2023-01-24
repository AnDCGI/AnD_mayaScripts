#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
'''Clean Unknown Plugins
This Script Will Delete Any Unknown Plugins From Maya Scene
The List of Deleted Plugins Can Be Seen On Maya Script Editor
'''
import maya.cmds as cmds

cmds.delete(cmds.ls(type="unknown"))
plg_ls = cmds.unknownPlugin(q=True, l=True)
if plg_ls:
    for plugin in plg_ls:
        print(plugin)
        cmds.unknownPlugin(plugin, r=True)
'''
A Pre-maya 6.5 File That Contains References Is Converted To A Later Version
Maya File, A Reference Node Named "_unknown_ref_node_" May Be Created And/or
A Special "_unknown_ref_node_" Entry May Be Added To Existing Reference Nodes.
This Node Type Was Used To Store Any Edits That Were Made Prior To 6.5
Until Those Edits Could Be Applied.
Once All References In The Scene Have Been Loaded, All Edits Should Be Applied
And The _unknown_ref_node_ Areas And Nodes Should Disappear. If There Are Any
Edits Which Can Not Be Applied (for Example, Nodes In The Original Reference
File That Were Renamed Or Deleted), The _unknown_ref_node_ Will Remain In The
File.
If You Need To Remove These Reference Nodes, You Can Do So By Querying For
The _unknown_ref_node_ And Deleting It. That Is, This Specific Node Type
Cannot Be Deleted Using The Reference Editor.
'''
# Use The Bottom Line Only If You Have "_UNKNOWN_REF_NODE_"
if '_UNKNOWN_REF_NODE_' in cmds.ls(type='reference'):
    cmds.delete("_UNKNOWN_REF_NODE_")
