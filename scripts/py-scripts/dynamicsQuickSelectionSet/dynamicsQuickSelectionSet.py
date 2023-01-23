#!/usr/bin/env python3
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

version = 1.0
winID_A = 'QSS Create'  # Declaring Window ID

if cmds.window(winID_A, exists=True):  # Check To See If Window Exists
    cmds.deleteUI(winID_A)

# Defines Create Button Action


def CreateButtonPush(*args):
    currentValue = cmds.optionMenu('Object_Type', query=True, value=True)

    # For Fluid Emitters
    if currentValue == 'Fluid Emitter':
        set = cmds.ls(type='fluidEmitter')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('fluidEmitterQSS'):
                cmds.sets(set, include='fluidEmitterQSS')
            else:
                cmds.sets(name='fluidEmitterQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Fluid Emitter</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Fluid Emitter Not Found!',
                               button='Yes I Acknowledge')

# For Particles Emitters
    elif currentValue == 'nParticle/Particle Emitter':
        set = cmds.ls(exactType='pointEmitter')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('particleEmitterQSS'):
                cmds.sets(set, include='particleEmitterQSS')
            else:
                cmds.sets(name='particleEmitterQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Particle Emitter</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Particle Emitter Not Found!',
                               button='Yes I Acknowledge')

# For nRigids
    elif currentValue == 'nRigid':
        set = cmds.ls(type='nRigid')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('nRigidQSS'):
                cmds.sets(set, include='nRigidQSS')
            else:
                cmds.sets(name='nRigidQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg='Created Quick Selection Set with all <hl>nRigid</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='nRigid Not Found!',
                               button='Yes I Acknowledge')

# For Fluid Containers
    elif currentValue == 'Fluid Container':
        set = cmds.ls(type='fluidShape')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('fluidShapeQSS'):
                cmds.sets(set, include='fluidShapeQSS')
            else:
                cmds.sets(name='fluidShapeQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Fluid Container</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Fluid Container Not Found!',
                               button='Yes I Acknowledge')

# For Nucleus Solvers
    elif currentValue == 'Nucleus':
        set = cmds.ls(type='nucleus')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('nucleusQSS'):
                cmds.sets(set, include='nucleusQSS')
            else:
                cmds.sets(name='nucleusQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg='Created Quick Selection Set with all <hl>Nucleus</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Nucleus Not Found!',
                               button='Yes I Acknowledge')

# For nParticles
    elif currentValue == 'nParticle':
        set = cmds.ls(type='nParticle')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('nParticleQSS'):
                cmds.sets(set, include='nParticleQSS')
            else:
                cmds.sets(name='nParticleQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>nParticle</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='nParticle Not Found!',
                               button='Yes I Acknowledge')

# For Force Fields
    elif currentValue == 'Force Field':
        set = cmds.ls(type='field')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('forceFieldQSS'):
                cmds.sets(set, include='forceFieldQSS')
            else:
                cmds.sets(name='forceFieldQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Force Field</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Force Field Not Found!',
                               button='Yes I Acknowledge')

# For Legacy Particles
    elif currentValue == 'Legacy Particle':
        set = cmds.ls(exactType='particle')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('ParticleQSS'):
                cmds.sets(set, include='ParticleQSS')
            else:
                cmds.sets(name='ParticleQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Legacy Particle</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Legacy Particle Not Found!',
                               button='Yes I Acknowledge')

# For nCloths
    elif currentValue == 'nCloth':
        set = cmds.ls(exactType='nCloth')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('nClothQSS'):
                cmds.sets(set, include='nClothQSS')
            else:
                cmds.sets(name='nClothQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg='Created Quick Selection Set with all <hl>nCloth</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='nCloth Not Found!',
                               button='Yes I Acknowledge')

# For Dynamic Constraints
    elif currentValue == 'Dynamic Constraint':
        set = cmds.ls(exactType='dynamicConstraint')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('dynamicConstraintQSS'):
                cmds.sets(set, include='dynamicConstraintQSS')
            else:
                cmds.sets(name='dynamicConstraintQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Dynamic Constraint</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Dynamic Constraint Not Found!',
                               button='Yes I Acknowledge')

# For Rigid Bodies
    elif currentValue == 'Rigid Body':
        set = cmds.ls(exactType='rigidBody')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('rigidBodyQSS'):
                cmds.sets(set, include='rigidBodyQSS')
            else:
                cmds.sets(name='rigidBodyQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Rigid Bodie</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Rigid Body Not Found!',
                               button='Yes I Acknowledge')

# For Rigid Constraints
    elif currentValue == 'Rigid Constraint':
        set = cmds.ls(exactType='rigidConstraint')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('rigidConstraintQSS'):
                cmds.sets(set, include='rigidConstraintQSS')
            else:
                cmds.sets(name='rigidConstraintQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Rigid Constraint</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Rigid Constraint Not Found!',
                               button='Yes I Acknowledge')

# For Anim Constraints
    elif currentValue == 'Anim Constraint':
        set = cmds.ls(type='constraint')
        if bool(set):  # Condition If No Objects Type In Scene
            cmds.select(set)
            if cmds.objExists('constraintQSS'):
                cmds.sets(set, include='constraintQSS')
            else:
                cmds.sets(name='constraintQSS', text='gCharacterSet')
                cmds.inViewMessage(
                    amg=
                    'Created Quick Selection Set with all <hl>Anim Constraint</hl>',
                    pos='midCenter',
                    font="Cascadia Mono SemiBold",
                    fade=True)
        else:
            cmds.confirmDialog(title='Warning',
                               icn='warning',
                               message='Anim Constraint Not Found!',
                               button='Yes I Acknowledge')


# Defines Done Button Action


def DoneButtonPush(*args):
    cmds.deleteUI(window, window=True)


# Creates Actual Window GUI
window = cmds.window(winID_A,
                     title='FX Quick Selection Set',
                     resizeToFitChildren=True,
                     sizeable=False,
                     tlb=True)

# Creates Layout
cmds.frameLayout(label='Dynamics Quick Selection Set Options',
                 collapsable=False,
                 mw=5,
                 mh=5)
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
cmds.rowLayout(numberOfColumns=2,
               columnWidth2=(117, 117),
               columnAttach=[(1, 'both', 0), (2, 'both', 0)])
cmds.button(label='Create', command=CreateButtonPush)
cmds.button(label='Done', command=DoneButtonPush)

# Shows Window
cmds.showWindow()
