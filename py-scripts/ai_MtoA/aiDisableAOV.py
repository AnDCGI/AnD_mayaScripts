# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

import maya.cmds as mc      # Importing The Main Maya Python Module

# Getiing All AOVs In The Scene
aovList = mc.ls(type="aiAOV")
for node in aovList:
    # This Sets The Enable Disable Status
    mc.setAttr(node+".enabled", False)
    # Prints List Of AOVs That's Been Truned Off
    print("Turned Off " + node)
