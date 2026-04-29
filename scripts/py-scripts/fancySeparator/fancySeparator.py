#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Â© 2019 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
Fancy Separator. This script is intended to function as a shelf button within Maya, opening a pop-up window with all of 
the predefined shelf icons. The user can use the icons given or choose own icons as well. The separator has very little 
width, therefore depending on the custom image, custom icon separator may appear distorted.

Original MEL script by Giuseppe Russo, thanks sharing it with the community. Modified to work on Python 3.
"""

import maya.cmds as cmds  # Importing The Main Maya Python Module
import maya.mel as mel  # Importing The Mel Python Wrapper Module

VERSION = 1.0
WINDOW_ID = 'separatorUI'  # Declaring Window ID

if cmds.window(WINDOW_ID, ex=1):
    cmds.deleteUI(WINDOW_ID)
    cmds.windowPref(WINDOW_ID, remove=1)


def addSeparator(color, custom):
    mel.eval('global string $gShelfTopLevel')
    # Get the Current Active Shelf
    ActiveShelf = str(cmds.tabLayout(mel.eval('$temp=$gShelfTopLevel'), q=1, selectTab=1))
    # For Custom Icon
    icon = ''
    if custom == 0:
        icon = 'separatorIcons/' + color + '.png'
    elif color == '':
        cmds.error('Please select an icon')
    else:
        icon = color
    cmds.shelfButton(style='iconOnly',
                     enable=1,
                     parent=ActiveShelf,
                     visible=1,
                     image=icon,
                     manage=1,
                     height=32,
                     width=10,
                     command=lambda *args: mel.eval('separatorUI'),
                     label='customSeparator',
                     annotation='Separator',
                     doubleClickCommand=lambda *args: mel.eval('separatorUI()'))
    print('\nSeparator Added!')


def addCustomSeparator(*args):
    selection = cmds.fileDialog2(fileFilter='PNG files (*.png)', fileMode=1)
    if selection:
        addSeparator(selection[0], 1)


cmds.window(WINDOW_ID,
            maximizeButton=False,
            sizeable=False,
            resizeToFitChildren=True,
            title='Create Separator | v{}'.format(VERSION),
            tlb=True)

# For Custom Image
cmds.rowColumnLayout()
cmds.button(command=addCustomSeparator, label='Custom Icon')
cmds.setParent('..')
# Grid Layout
cmds.gridLayout(numberOfColumns=5, ag=True, cellWidthHeight=(65, 60))
# Line 1 Images
cmds.iconTextButton(c=lambda *args: addSeparator('turquoise', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/turquoise.png',
                    label='Turquoise')
cmds.iconTextButton(c=lambda *args: addSeparator('emerald', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/emerald.png',
                    label='Emerald')
cmds.iconTextButton(c=lambda *args: addSeparator('peterriver', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/peterriver.png',
                    label='Peter River')
cmds.iconTextButton(c=lambda *args: addSeparator('amethyst', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/amethyst.png',
                    label='Amethyst')
cmds.iconTextButton(c=lambda *args: addSeparator('wetasphalt', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/wetasphalt.png',
                    label='Wet Asphalt')
# Line 2 Images
cmds.iconTextButton(c=lambda *args: addSeparator('sunflower', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/sunflower.png',
                    label='Sunflower')
cmds.iconTextButton(c=lambda *args: addSeparator('carrot', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/carrot.png',
                    label='Carrot')
cmds.iconTextButton(c=lambda *args: addSeparator('alizarin', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/alizarin.png',
                    label='Alizarin')
cmds.iconTextButton(c=lambda *args: addSeparator('clouds', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/clouds.png',
                    label='Clouds')
cmds.iconTextButton(c=lambda *args: addSeparator('concrete', 0),
                    style='iconAndTextVertical',
                    image='separatorIcons/concrete.png',
                    label='Concrete')
cmds.setParent('..')
cmds.showWindow()

