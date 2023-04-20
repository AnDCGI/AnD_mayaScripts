#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2019 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
"""
Fancy Separator. This script is intended to function as a shelf button within Maya, opening a pop-up window with all of 
the predefined shelf icons. The user can use the icons given or choose own icons as well. The separator has very little 
width, therefore depending on the custom image, custom icon separator may appear distorted.

Original MEL script by Giuseppe Russo, thanks sharing it with the community. Modified to work on Python 3.
"""

import maya.cmds as cmds  # Importing The Main Maya Python Module
import maya.mel as mel  # Importing The Mel Python Wrapper Module

version = 1.0
windowNameSeparator = 'separatorUI'  # Declaring Window ID

if cmds.window(windowNameSeparator, ex=1):
    cmds.deleteUI(windowNameSeparator)
    cmds.windowPref(windowNameSeparator, remove=1)


def addSeparator(color, custom):
    mel.eval('global string $gShelfTopLevel')
    # Get the Current Active Shelf
    ActiveShelf = str(cmds.tabLayout(mel.eval('$temp=$gShelfTopLevel'), q=1, selectTab=1))
    # For Custom Icon
    icon = ''
    if custom == 0:
        icon = 'separatoricons/' + color + '.png'
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


cmds.window(windowNameSeparator,
            maximizeButton=False,
            sizeable=False,
            resizeToFitChildren=True,
            title='Create Separator',
            tlb=True)

# For Custom Image
cmds.rowColumnLayout()
cmds.button(c=lambda *args: cmds.evalDeferred(lambda: addSeparator(
    cmds.fileDialog2(fileFilter='*.png')[0] if cmds.fileDialog2(ff='PNG files (*.png)', fm=1) else None, 1)),
            l='Custom Icon')
cmds.setParent('..')
# Grid Layout
cmds.gridLayout(numberOfColumns=5, ag=True, cellWidthHeight=(65, 60))
# Line 1 Images
cmds.iconTextButton(c=lambda *args: addSeparator('turquoise', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/turquoise.png',
                    label='Turquoise')
cmds.iconTextButton(c=lambda *args: addSeparator('emerald', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/emerald.png',
                    label='Emerald')
cmds.iconTextButton(c=lambda *args: addSeparator('peterriver', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/peterriver.png',
                    label='Peter River')
cmds.iconTextButton(c=lambda *args: addSeparator('amethyst', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/amethyst.png',
                    label='Amethyst')
cmds.iconTextButton(c=lambda *args: addSeparator('wetasphalt', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/wetasphalt.png',
                    label='Wet Asphalt')
# Line 2 Images
cmds.iconTextButton(c=lambda *args: addSeparator('sunflower', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/sunflower.png',
                    label='Sunflower')
cmds.iconTextButton(c=lambda *args: addSeparator('carrot', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/carrot.png',
                    label='Carrot')
cmds.iconTextButton(c=lambda *args: addSeparator('alizarin', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/alizarin.png',
                    label='Alizarin')
cmds.iconTextButton(c=lambda *args: addSeparator('clouds', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/clouds.png',
                    label='Clouds')
cmds.iconTextButton(c=lambda *args: addSeparator('concrete', 0),
                    style='iconAndTextVertical',
                    image='separatoricons/concrete.png',
                    label='Concrete')
cmds.setParent('..')
cmds.showWindow()