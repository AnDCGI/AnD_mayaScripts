"""Open the project GitHub page in Maya's default browser."""

import maya.cmds as cmds


def showHelp():
    cmds.showHelp("https://github.com/AnDCGI", absolute=True)
