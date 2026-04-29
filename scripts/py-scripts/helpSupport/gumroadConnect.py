"""Open the Gumroad support page in Maya's default browser."""

import maya.cmds as cmds


def showHelp():
    cmds.showHelp("https://andlabs.gumroad.com/coffee", absolute=True)
