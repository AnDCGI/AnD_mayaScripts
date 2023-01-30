#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
Maya Broadcast FPS. This script is designed to work as a shelf button inside maya which will open a pop-up window with 
all the presets. The tool changes the FPS based on selected preset, although kind of a similar option is available 
inside Maya the problem is timeline and time slider goes into float values, this fixes that also sets the Start & End 
as user defined values respectively.

Disclaimer! This doesn't change any keyframe nor convert FPS, it just sets FPS, meant to be used on an empty scene
"""

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


def SetButtonPush(*args):
    """
    This function sets the frames per second (FPS) based on the selected option in the option menu.
    It also starts the playback and displays a message in the viewport to indicate the FPS change.
    """
    # Get Selected FPS Value From Option Menu
    currentValue = cmds.optionMenu('Select_FPS', query=True, value=True)
    # Get Start & End Frame Values From the Int Fields
    cMinTime = cmds.intField('strtFrame', query=True, value=True)
    cMaxTime = cmds.intField('endFrame', query=True, value=True)

    # Set FPS & Start, End Frame Based on Selected Value
    if currentValue == 'Game 15 FPS':
        setFPS(cMinTime, cMaxTime, 'game', 15)
    elif currentValue == 'Film 24 FPS':
        setFPS(cMinTime, cMaxTime, 'film', 24)
    elif currentValue == 'PAL/SECAM 25 FPS':
        setFPS(cMinTime, cMaxTime, 'pal', 25)
    elif currentValue == 'NTSC 30 FPS':
        setFPS(cMinTime, cMaxTime, 'ntsc', 30)
    elif currentValue == 'Show 48 FPS':
        setFPS(cMinTime, cMaxTime, 'show', 48)
    elif currentValue == 'PAL F 50 FPS':
        setFPS(cMinTime, cMaxTime, 'palf', 50)
    elif currentValue == 'NTSC F 60 FPS':
        setFPS(cMinTime, cMaxTime, 'ntscf', 60)


def setFPS(cMinTime, cMaxTime, unit, fps):
    """
    This function sets the FPS, starts the playback and displays a message in the viewport

    :param cMinTime: Gets the Start Frame Number
    :param cMaxTime: Gets the End Frame Number
    :param unit: Gets the Unit i.e. game, film etc
    :param fps: Gets the fps for that unit
    """
    mel.eval(f'currentUnit -time {unit}')
    mel.eval('playbackOptions -ps 0')
    mel.eval(f'playbackOptions -e -ast {cMinTime}-min {cMinTime}-max {cMaxTime}-aet {cMaxTime}')
    mel.eval('playButtonStart')
    cmds.inViewMessage(amg=f'Changed FPS to <hl>{fps}</hl>', pos='midCenter', font="Cascadia Mono SemiBold", fade=True)


# Creates Actual Window
window = cmds.window(winID, title='Maya FPS Switch', resizeToFitChildren=True, sizeable=False, tlb=True)

# Creates Layout
cmds.frameLayout(label='Broadcast FPS Options', collapsable=False, mw=5, mh=5)
cmds.text(label='AnD CGI CC BY-SA 4.0', font='smallPlainLabelFont')
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
