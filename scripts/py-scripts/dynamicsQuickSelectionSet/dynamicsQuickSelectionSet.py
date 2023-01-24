#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
'''Dynamics Quick Selection Set
 This Tool Collects Different Types of Objects* by Searching the Whole Scene
 User Have to Choose the Type of Object, Click Create & the Tool Will Create An
 Quick Selection Set
 Every Quick Selection Set Will Have a QSS Suffix

*Drop Down Options are Related to FX Only'''

import maya.cmds as cmds  # Importing The Main Maya Python Module

version = 1.1
winID_A = 'QSS Create'  # Declaring Window ID

if cmds.window(winID_A, exists=True):  # Check To See If Window Exists
    cmds.deleteUI(winID_A)

# Defines Create Button Action


def CreateButtonPush(*args):
    currentValue = cmds.optionMenu('Object_Type', query=True, value=True)
    set = None
    qssName = None
    notFoundMessage = "{} Not Found!".format(currentValue)
    creationMessage = "Created Quick Selection Set with all <hl>{}</hl>".format(currentValue)

    # For Fluid Emitters
    if currentValue == 'Fluid Emitter':
        set = cmds.ls(type='fluidEmitter')
        qssName = 'fluidEmitterQSS'

    # For Particles Emitters
    elif currentValue == 'nParticle/Particle Emitter':
        set = cmds.ls(exactType='pointEmitter')
        qssName = 'particleEmitterQSS'

    # For nRigids
    elif currentValue == 'nRigid':
        set = cmds.ls(type='nRigid')
        qssName = 'nRigidQSS'

    # For Fluid Containers
    elif currentValue == 'Fluid Container':
        set = cmds.ls(type='fluidShape')
        qssName = 'fluidShapeQSS'

    # For Nucleus Solvers
    elif currentValue == 'Nucleus':
        set = cmds.ls(type='nucleus')
        qssName = 'nucleusQSS'

    # For nParticles
    elif currentValue == 'nParticle':
        set = cmds.ls(type='nParticle')
        qssName = 'nParticleQSS'

    # For Force Fields
    elif currentValue == 'Force Field':
        set = cmds.ls(type='field')
        qssName = 'forceFieldQSS'

    # For Legacy Particles
    elif currentValue == 'Legacy Particle':
        set = cmds.ls(exactType='particle')
        qssName = 'ParticleQSS'

    # For nCloths
    elif currentValue == 'nCloth':
        set = cmds.ls(exactType='nCloth')
        qssName = 'nClothQSS'

    # For Dynamic Constraints
    elif currentValue == 'Dynamic Constraint':
        set = cmds.ls(exactType='dynamicConstraint')
        qssName = 'dynamicConstraintQSS'

    # For Rigid Bodies
    elif currentValue == 'Rigid Body':
        set = cmds.ls(exactType='rigidBody')
        qssName = 'rigidBodyQSS'

    # For Rigid Constraints
    elif currentValue == 'Rigid Constraint':
        set = cmds.ls(exactType='rigidConstraint')
        qssName = 'rigidConstraintQSS'

    # For Anim Constraints
    elif currentValue == 'Anim Constraint':
        set = cmds.ls(type='constraint')
        qssName = 'constraintQSS'

    if bool(set):
        cmds.select(set)
        if cmds.objExists(qssName):
            cmds.sets(set, include=qssName)
        else:
            cmds.sets(name=qssName, text='gCharacterSet')
            cmds.inViewMessage(amg=creationMessage, pos='midCenter', font="Cascadia Mono SemiBold", fade=True)
    else:
        cmds.confirmDialog(title='Warning', icn='warning', message=notFoundMessage, button='Yes I Acknowledge')


# Defines Done Button Action
def DoneButtonPush(*args):
    cmds.deleteUI(window, window=True)


# Creates Actual Window GUI
window = cmds.window(winID_A, title='FX Quick Selection Set', resizeToFitChildren=True, sizeable=False, tlb=True)

# Creates Layout
cmds.frameLayout(label='Dynamics Quick Selection Set Options', collapsable=False, mw=5, mh=5)
cmds.text(label='© AnD CGI CC BY-SA 4.0', font='smallPlainLabelFont')
cmds.columnLayout()
cmds.optionMenu('Object_Type', label='Object Type')
cmds.menuItem(label=" ")
cmds.menuItem(label='Fluid Emitter')
cmds.menuItem(label='nParticle/Particle Emitter')
cmds.menuItem(label='Fluid Container')
cmds.menuItem(label='nRigid')
cmds.menuItem(label='nCloth')
cmds.menuItem(label='nParticle')
cmds.menuItem(label='Rigid Body')
cmds.menuItem(label='Legacy Particle')
cmds.menuItem(label='Dynamic Constraint')
cmds.menuItem(label='Rigid Constraint')
cmds.menuItem(label='Anim Constraint')
cmds.menuItem(label='Force Field')
cmds.menuItem(label='Nucleus')

# Creates Buttons
cmds.rowLayout(numberOfColumns=2, columnWidth2=(117, 117), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
cmds.button(label='Create', command=CreateButtonPush)
cmds.button(label='Done', command=DoneButtonPush)

# Shows Window
cmds.showWindow()
