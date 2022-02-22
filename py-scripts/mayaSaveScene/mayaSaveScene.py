#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
'''Maya Save Scene
This Is Especially Ment To Work With Cache Pipeline, Where The User
Builds The Cache, Camera Name Contains Scene Name & The Direcoty Of File Is
Always Set And Definened By Specific Strucure
Here This Script Will Automatically Get The Save Location Based On The
Name Of The Camera And Create A Folder And Save The File Inside If The File
Already Exsist It Will Do A Version Up And Save
'''
# Importing Modules
import maya.cmds as cmds    # Importing The Main Maya Python Module
import os   # Getting The OS Module For Path Manipulation

# Declaring Varibale
vNum = str(1)
globalPath = "A:\\01prj\\XYZ\\prod\\shotpub"    # Path To Global Directory

# Finding Cameras
cameras = cmds.listCameras(p=True)
exclude = ["persp"]
# Getting Nothing But The User Camera
cameras = list(set(cameras) - set(exclude))

# Fixing Camera Name As Per Need
camName = cameras[0]
# String Deletation Needs To Be Set As Per User Directory Char Count
camName = camName[3:21]
camPath = camName.replace("_", "\\")

# Having Save Directory
saveDir = globalPath + camPath

# Giving Folder Name Where The File Will Be Saved
directory = "fx_scene"
path = os.path.join(saveDir, directory)

# Skipping If Folder Exists
if not os.path.exists(path):
    os.makedirs(path)

# Creating The Total Path
saveDir = globalPath + camPath + "\\" + "fx_scene\\"
fileName = saveDir.replace("\\", "_")
# String Deletation Needs To Be Set As Per User Directory Char Count
fileName = "aaj" + fileName[-28:] + "source" + "_v" + vNum.zfill(3) + ".ma"
# The Final File Path For New File
mergeSDFN = saveDir + fileName

# Version Up If File Already There
if os.path.isfile(mergeSDFN):
    getFileName = cmds.file(q=True, sn=True).split('/')[-1]
    # String Deletation Needs To Be Set As Per User Directory Char Count
    getVName = int(getFileName[-6:-3])
    newVNum = getVName + 1
    newVNum = str(newVNum)
    newFName = getFileName[:-6] + newVNum.zfill(3) + ".ma"
    newMergeSDFN = saveDir + newFName
    cmds.file(rename=newMergeSDFN)
    cmds.file(save=True, type="mayaAscii")
# Save For New Scene
else:
    cmds.file(rename=mergeSDFN)
    cmds.file(save=True, type="mayaAscii")
