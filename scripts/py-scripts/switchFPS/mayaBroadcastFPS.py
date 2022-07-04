#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
'''Maya Broadcast FPS
This Script Designed To Work As A Shelf Button Inside Maya Which Will Open A
New Pop Up UI With All The Presets. The Tool Changes The FPS Based On Selected
Preset Althogh Kind Of A Similar Option Is Avilavle Inside Maya But The
Timeline And Timeslider Goes Into Float Values, This Fixes That Also Sets The
Start & End As 101 - 500 Respectively Which Can Be Changed By Changing The
Values Inside The Code

DISCLAIMER This Doesnt Changes Any Keyframe Nor Converts FPS, It Just Sets FPS,
Meant To Be Used On A Empty Scene'''

import maya.cmds as cmds  # Importing The Main Maya Python Module
import maya.mel as mel  # Importing The Mel Python Wrapper Module

version = 1.0
winID = 'SetDesiredFPS'  # Declaring Window ID

cAnimationStartTime = cmds.playbackOptions(q=True, ast=True)  # Gets The Start
cAnimationEndTime = cmds.playbackOptions(q=True, aet=True)  # Gets The End
cMinTime = cAnimationStartTime  # Sets The Start Of The Playback Time Range
cMaxTime = cAnimationEndTime  # Sets The End Of The Playback Time Range

if cmds.window(winID, exists=True):  # Check To See If Window Exists
    cmds.deleteUI(winID)

# Defines Set Button Action


def SetButtonPush(*args):

    currentValue = cmds.optionMenu('Select_FPS', query=True, value=True)
    cMinTime = cmds.intField('strtFrame', query=True, value=True)
    cMaxTime = cmds.intField('endFrame', query=True, value=True)

    if currentValue == 'Game 15 FPS':
        mel.eval('currentUnit -time game')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>15</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)
    elif currentValue == 'Film 24 FPS':
        mel.eval('currentUnit -time film')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>24</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)
    elif currentValue == 'PAL/SECAM 25 FPS':
        mel.eval('currentUnit -time pal')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>25</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)
    elif currentValue == 'NTSC 30 FPS':
        mel.eval('currentUnit -time ntsc')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>30</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)
    elif currentValue == 'Show 48 FPS':
        mel.eval('currentUnit -time show')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>48</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)
    elif currentValue == 'PAL F 50 FPS':
        mel.eval('currentUnit -time palf')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>50</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)
    elif currentValue == 'NTSC F 60 FPS':
        mel.eval('currentUnit -time ntscf')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast ' + str(cMinTime) + '-min ' +
                 str(cMinTime) + '-max ' + str(cMaxTime) + '-aet ' +
                 str(cMaxTime))
        mel.eval('playButtonStart')
        cmds.inViewMessage(amg='Changed FPS to <hl>60</hl>',
                           pos='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True)


# Creates Actual Window
window = cmds.window(winID,
                     title='Maya FPS Switch',
                     resizeToFitChildren=True,
                     sizeable=False,
                     tlb=True)

# Creates Layout
cmds.frameLayout(label='Broadcast FPS Options', collapsable=False, mw=5, mh=5)
cmds.text(label='© AnD CGI CC BY-SA 4.0', font='smallPlainLabelFont')
cmds.columnLayout()
cmds.optionMenu('Select_FPS', label='Select FPS')
cmds.menuItem(label=" ")
cmds.menuItem(label='Game 15 FPS')
cmds.menuItem(label='Film 24 FPS')
cmds.menuItem(label='PAL/SECAM 25 FPS')
cmds.menuItem(label='NTSC 30 FPS')
cmds.menuItem(label='Show 48 FPS')
cmds.menuItem(label='PAL F 50 FPS')
cmds.menuItem(label='NTSC F 60 FPS')
cmds.setParent('..')

# Creates Frame Input Fields
cmds.rowLayout(numberOfColumns=3)
cmds.text(label='Start Frame')
cmds.text(label='', width=5)
cmds.intField('strtFrame', value=cAnimationStartTime)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=3)
cmds.text(label='End Frame')
cmds.text(label='', width=9)
cmds.intField('endFrame', value=cAnimationEndTime)
cmds.setParent('..')

# Creates Buttons
cmds.rowLayout(numberOfColumns=2)
cmds.text(label='', width=46)
cmds.button(label='Set', command=SetButtonPush, w=100)
cmds.setParent('..')

# Shows Window
cmds.showWindow()
