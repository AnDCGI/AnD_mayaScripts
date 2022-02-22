# © 2020 AnD CGI This work is licensed under a Creative Commons
# Attribution-ShareAlike 4.0 International License.
''' Maya One Click Scene Scale Change
This Script Is Designed To Change Scene Scale Like For FX, Lighting Etc.
Designed To Work As A Shelf Button Inside Maya And Especially Made To Work With
Alembic Files. By Default It Will Scale Everything Down To 0.1 In All Axis,
User Can Later Change The Scale At Any Point. This Is A Headless Script So
Watch Out For In View Message
'''

import maya.cmds as cmds  # Importing The Main Maya Python Module
import maya.mel as mel  # Importing The Mel Python Wrapper Module

# Selecting Everything Inside Scene Then Getting Transform Node
cmds.select(all=True, hierarchy=True)
selection = cmds.ls(selection=True)
transformNode = cmds.listRelatives(selection, p=True)

for obj in transformNode:  # Setting Inherit Transform On For Alembic Files
    # Skip This Block While Working With Regular Files
    cmds.setAttr(obj + ".inheritsTransform", 1)

cmds.select(all=True)  # Selecting Everything Inside Scene Again
selection = cmds.ls(selection=True)

# Creating Locator, Renaming & Making It Parent Of Everything Inside Scene
locator = cmds.spaceLocator()
cmds.parent(selection, locator)
cmds.select(locator)
cmds.rename(locator, 'sceneScale')

# Setting Scene Scale, Here Default Is 0.1
cmds.setAttr("sceneScale.scaleX", 0.1)
cmds.setAttr("sceneScale.scaleY", 0.1)
cmds.setAttr("sceneScale.scaleZ", 0.1)

# Hiding Traslate
cmds.setAttr("sceneScale.translateX", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.translateY", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.translateZ", keyable=False, cb=False, lock=True)

# Hiding Rotate
cmds.setAttr("sceneScale.rotateX", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.rotateY", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.rotateZ", keyable=False, cb=False, lock=True)

# Hiding Local Position
cmds.setAttr("sceneScale.localPositionX", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.localPositionY", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.localPositionZ", keyable=False, cb=False, lock=True)

# Hiding Local Scale
cmds.setAttr("sceneScale.localScaleX", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.localScaleY", keyable=False, cb=False, lock=True)
cmds.setAttr("sceneScale.localScaleZ", keyable=False, cb=False, lock=True)

# Some Beautification Of The Locator So It Stands Out
cmds.setAttr("sceneScale.useOutlinerColor", 1)
cmds.setAttr("sceneScale" + ".outlinerColor", 0, 1, 0)
cmds.setAttr("sceneScale.overrideEnabled", 1)
cmds.setAttr("sceneScale" + ".overrideColor", 13)

# Refreshing Outliner & Attribute Editor So That It Can Reflects The Change
mel.eval('AEdagNodeCommonRefreshOutliners()')
mel.eval('AttributeEditor;updateAE("sceneScale")')

# Some Message
cmds.inViewMessage(amg='New Scene Scale <hl>0.1</hl>',
                   pos='midCenter', font="Cascadia Mono SemiBold", fade=True)
