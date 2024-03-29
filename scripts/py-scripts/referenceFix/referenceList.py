#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# © 2022 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.

import os
import re
import maya.cmds as cmds
import logging

logging.basicConfig(level=logging.DEBUG, filename="error.log")
version = '1.0.1'
winID = 'RefError'  # Declaring Window ID

if cmds.window(winID, exists=True):  # Check To See If Window Exists
    cmds.deleteUI(winID)


def LoadMayaFilesDir(*args):
    fDir = cmds.fileDialog2(dialogStyle=2,
                            caption='Select Maya Files Directory',
                            fileMode=3,
                            okCaption='Accept',
                            returnFilter=True)[0]
    cmds.textFieldGrp(fText, text=fDir, e=1)


def ReferenceFilesDir(*args):
    rDir = cmds.fileDialog2(dialogStyle=2,
                            caption='Select Reference Files Directory',
                            fileMode=3,
                            okCaption='Accept',
                            returnFilter=True)[0]
    cmds.textFieldGrp(rText, text=rDir, e=1)


def FindMayaFiles(filesDir):
    filePaths = []
    filesDir = os.path.join(filesDir, '')
    for dirpath, dirnames, filenames in os.walk(filesDir):
        for filename in filenames:
            if filename.endswith('.ma'):
                filePaths.append(os.path.join(dirpath, filename))
    return filePaths


def SearchReturnLines(listPath, searchString):
    resultLines = []
    with open(listPath, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if searchString in line:
                if (i + 1) < len(lines) and not lines[i + 1].startswith(searchString):
                    resultLines.append(line.strip() + ' ' + lines[i + 1])
                else:
                    resultLines.append(line.strip())
    return resultLines


def RunButtonPush(*args):
    currentValue = cmds.radioButtonGrp('Radio_Type', query=True, select=True)
    filesDir = cmds.textFieldGrp('Path_Text', query=True, fileName=True)
    refrDir = cmds.textFieldGrp('Ref_Text', query=True, fileName=True)

    if filesDir != '' and refrDir != '':
        # Create a List From Given Directory
        fp = FindMayaFiles(filesDir)

        # For Text Generation
        if currentValue == 1:
            promptValue = cmds.file(q=True, prompt=True)  # Warning Or PopUp Message Option
            cmds.file(prompt=False)  # Warning Or PopUp Message Off

            for fi in fp:
                refNodes = []

                refList = open(fi[:-3] + ' - FAIL.txt', 'w')
                cmds.file(new=True, force=True)
                cmds.file(fi, open=True, force=True, loadReferenceDepth='none', buildLoadSettings=False)

                # Getting All Reference Node Names
                for node in cmds.ls(type='reference'):
                    if 'sharedReferenceNode' in node:
                        continue
                    if '_UNKNOWN_REF_NODE_' in node:
                        continue
                    else:
                        refNodes.append(node)

                # Getting All Reference File Paths
                for ref in refNodes:
                    if refrDir in cmds.referenceQuery(ref, filename=True):
                        noRefList = open(fi[:-3] + ' - PASS.txt', 'w')
                        noRefList.close()
                    else:
                        refList.write(cmds.referenceQuery(ref, filename=True) + '\n')

                refList.close()

                try:
                    if os.path.getsize(fi[:-3] + ' - FAIL.txt') > 0:
                        pass
                    else:
                        os.remove(fi[:-3] + ' - FAIL.txt')
                except OSError as error:
                    print(error)

            cmds.file(prompt=promptValue)  # Warning Or PopUp Message Back On
            cmds.confirmDialog(title='Contribute',
                               message='Process Completed',
                               messageAlign='center',
                               button=['OK'],
                               defaultButton='Yes',
                               dismissString='No',
                               parent=winID)

        elif currentValue == 2:
            print('Not Ready!')

        elif currentValue == 3:
            matchedList = []

            for fi in fp:

                refList = open(fi[:-3] + ' - FAIL.txt', 'w')
                searchOutput = SearchReturnLines(fi, 'file ')

                for lines in searchOutput:
                    match = re.search(r'"([^"]*)"(?=;)', lines)
                    if match:
                        lastQuotedText = match.group(1)
                        matchedList.append(lastQuotedText)
                    else:
                        print("Possible Reference Pattern Error While Opening File as Text")

                matchedList = list(set(matchedList))  # Removing Duplicate Entries
                for ref in matchedList:
                    if refrDir in ref:
                        noRefList = open(fi[:-3] + ' - PASS.txt', 'w')
                        noRefList.close()
                    else:
                        refList.write(ref + '\n')

                refList.close()

                try:
                    if os.path.getsize(fi[:-3] + ' - FAIL.txt') > 0:
                        pass
                    else:
                        os.remove(fi[:-3] + ' - FAIL.txt')
                except OSError as error:
                    print(error)
            cmds.confirmDialog(title='Contribute',
                               message='Process Completed',
                               messageAlign='center',
                               button=['OK'],
                               defaultButton='Yes',
                               dismissString='No',
                               parent=winID)

    else:
        cmds.inViewMessage(assistMessage='<h1>Please Provide Valid Path</h1>',
                           position='midCenter',
                           font="Cascadia Mono SemiBold",
                           fade=True,
                           alpha=0.0)


# Creates Actual Window
window = cmds.window(winID,
                     title='Reference Error Checker | v' + version,
                     width=375,
                     height=180,
                     tlb=True,
                     sizeable=False)

# Creates Layout
cmds.frameLayout(label='Reference Error Options', collapsable=False, mw=5, mh=5)
cmds.text(label='AnD CGI CC BY-SA 4.0', font='smallPlainLabelFont')
cmds.setParent('..')
cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(1, 'both', 0), columnWidth=[(1, 100), (2, 250), (3, 25)])
cmds.text(label='Files Directory', font='boldLabelFont')
fText = cmds.textFieldGrp('Path_Text', width=100, placeholderText='Paste Maya Files Directory Here', text='')
cmds.iconTextButton(style='iconOnly', image1='loadPreset.xpm', label='loadPreset', command=LoadMayaFilesDir)
cmds.setParent('..')
cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(1, 'both', 0), columnWidth=[(1, 100), (2, 250), (3, 25)])
cmds.text(label='Reference Root', font='boldLabelFont')
rText = cmds.textFieldGrp('Ref_Text', width=100, placeholderText='Paste Reference Root Path Here', text='')
cmds.iconTextButton(style='iconOnly', image1='fileOpen.xpm', label='fileOpen', command=ReferenceFilesDir)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=4)
cmds.text(label='', width=25)
cmds.radioButtonGrp('Radio_Type',
                    labelArray3=['Maya (Slow)', 'Find/Replace', 'Pyhton (Fast)'],
                    numberOfRadioButtons=3,
                    enable=True,
                    select=1)
cmds.setParent('..')
cmds.separator(h=5)
cmds.rowLayout(numberOfColumns=4)
cmds.text(label='', width=87)
cmds.button(label='Run', width=100, command=RunButtonPush)
cmds.button(label='Close', width=100, command=('cmds.deleteUI(\"' + winID + '\", window=True)'))
cmds.text(label='', width=87)
cmds.setParent('..')
cmds.separator(h=5)
cmds.columnLayout(bgc=(1, 0, 0), columnOffset=('both', 85))
cmds.text(label='For Zoetrope Animation Studios By Dhruba', font='smallPlainLabelFont')
cmds.showWindow()