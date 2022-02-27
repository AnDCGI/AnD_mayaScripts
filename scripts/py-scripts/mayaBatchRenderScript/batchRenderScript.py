#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
'''The Batch Render Script
Designed To Work As A Shelf Button Inside Maya The Purpose Is To Work On As
Many Shots/files As Possible In A Shift After One File/shot Is Done Click On
The Shelf Button That Will Add It To An Auto Generated Batch File So At The End
Of The Shift User/artist Can Just Run The Batch File & All Added Shots Will Be
Rendered One After Another
'''
# Some Requirements For This To Work Is As Expected Are

# 1. Make Sure All Render Settings Are There Including Render Camera
# 2. Frame Range Is Set Inside Maya Render Settings
# 3. Ideally The Render Folder Directory Should Exits Before Hand If Not That
# Need To Be Created First
# 4. This Will Work With Any Render Engines, Make Sure To Have A "mayabatch"
# License

# This Is A Headless Script So Doesn't Prints Anything To Maya Command Line As
# Of Now

import maya.cmds as cmds    # Importing The Main Maya Python Module
import getpass      # To Attach Signature Of User
import sys      # Get System

insDir = sys.argv[0]
renDir = "\"" + str.replace(insDir, "maya", "Render") + "\""
# Where The Render Batch Script Will Be Generated
globalPath = "A:\\01prj\\XYZ\\prod\\assetbuildpub\\fx_assets\\BRScript\\"
print(globalPath)
# Getting The Maya File Path, Since The Batch Script Expects "" Thus Adding
mayaFilePath = "\"" + cmds.file(query=True, sceneName=True) + "\""
# Windows Path Replacing "/" With "\", Skip If Not Required
mayaFilePath = mayaFilePath.replace("/", "\\")
# Removing Some Character From The String & Adding Render Folder Location
# This Step Is Custom, Depends On How The Project Is Set, Change As Per Need
rndrFilePath = mayaFilePath[:44] + "/fx_renderLayers/v000\""
# Windows Path Replacing "/" With "\", Skip If Not Required
rndrFilePath = rndrFilePath.replace("/", "\\")

# Getting User Name, Uppercase All Letters & Keeping Only First And Last
# Character
userName = getpass.getuser()
userName = userName.upper()
userName = userName[0:1] + userName[-1:]

# The Batch File Will Have A Different Name Everyday, Thus Getting Date &
# Adding User Name With It
fileName = cmds.date(format="DD•MM•YYYY" + "_" + userName)

# Generating Batch File Also Appending Lines
fileHandle = open(globalPath + fileName + ".bat", "a+")

# Adding Lines One After Another, Thats How Maya Accepts The Batch File
fileHandle.write(renDir + " -r file -rd " + rndrFilePath + " " + mayaFilePath)
fileHandle.write("\n")
fileHandle.close()
