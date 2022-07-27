# Script Originaly Taken From Toadstorm Nerdblog, Everything is Untouched Fixed
# Few Discripencies

# This Script Takes Advantage of the Pickle Module to Store Variables to a Temporary
# File & Retrieve Them Later When Running Paste Operation
# Copy & Paste Between Separate Instances of Maya

'''Put the Script in Python Folder & Import It Like This:
import hfCopyPaste as hfCP


To Copy Channels, Highlight Them in Channel Box & Run:
hfCP.copyChan()


To Paste, Select Any Number of Objects & Run:
hfCP.pasteChan()
'''

# Edit Lines 44 & 65 For Custom Path, Make Sure Write Permission Present

import os
import pickle
import platform
import maya.cmds as cmds


def copyChan():     # The Copy Operation
    try:
        obj = cmds.ls(sl=1)[0]
    except IndexError:
        cmds.error('try selecting something.')
    xformChan = cmds.channelBox('mainChannelBox',q=1,sma=1)
    shapeChan = cmds.channelBox('mainChannelBox',q=1,ssa=1)
    objShape = cmds.channelBox('mainChannelBox',q=1,sol=1)
    bigPickle = []
    xDict = {}
    sDict = {}
    if xformChan != None:
        for a in xformChan:
            xDict[a] = cmds.getAttr(str(obj)+'.'+str(a))
    if shapeChan != None:
        for a in shapeChan:
            sDict[a] = cmds.getAttr(str(objShape[0])+'.'+str(a))

    # We Have Two Dictionaries of Transform Channels & Shape Channels. Writing
    # These to Disk So It Can Paste Between Instances of Maya.

    if platform.system() == 'Windows' or platform.system() == 'Microsoft':
        cppath = os.getcwd() + 'hfCopyPaste.txt'
    else:
        cppath = '/Users/Shared/hfCopyPaste.txt'
    clearfile = open(cppath, 'w')
    clearfile.close()       # Close File Immediately to Clear It.
    writefile = open(cppath, 'w')
    bigPickle.append(xDict)
    bigPickle.append(sDict)
    pickle.dump(bigPickle,writefile)
    writefile.close()
    print(xDict)
    print(sDict)
    cmds.inViewMessage(amg = 'Selected Channels Copied to Clipboard', pos = 'botCenter', fade = True)

def pasteChan():     # The Paste Operation
    objs = cmds.ls(sl=1)
    if len(objs) != 1:
        cmds.error('you should probably select something to paste to.')
    # load The Dicts Back From File To Apply Channels
    if platform.system() == 'Windows' or platform.system() == 'Microsoft':
        cppath = 'C:/TempX/hfCopyPaste.txt'
    else:
        cppath = '/Users/Shared/hfCopyPaste.txt'
    pastefile = open(cppath, 'r')
    # Index 0 is xform Channels. Index 1 is shape Channels.
    channels = pickle.load(pastefile)
    xDict = dict(channels[0])
    sDict = dict(channels[1])
    print('xDict')
    print('sDict')

    # Assign Each Channel to Every Object in Objs.
    for chan, value in xDict.iteritems():
        for obj in objs:
            try:
                cmds.setAttr(obj+'.'+chan, value)
            except:
                pass
    # Pasting Shape Values will be Trickier. Typically We are Only Selecting xforms.
    # We'll have to Get Any Associated Shapes with Each Obj in Objs & Paste Channels
    # to Them If Possible. Since we Don't Know Exactly What We're Pasting To Or
    # What We Copied From, We Should Just Try to Paste to Everything.

    # The Selected Objects & Their Shapes.
    allShapes = []
    allShapes.extend(objs)
    for obj in objs:
        shapes = cmds.listRelatives(obj,s=1)
        if shapes != None:
            allShapes.extend(shapes)
    for chan, value in sDict.iteritems():
        for shape in allShapes:
            try:
                cmds.setAttr(shape+'.'+chan, value)
            except:
                pass
    print('Channels Pasted to %d Objects' % len(objs))


