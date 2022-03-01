# Licensed under the MIT license

import os
import maya.cmds as cmds
import maya.mel as mel


def load():
    homeDir = os.path.expanduser('~')
    homeDir += "/Documents/"

    # Shelf to load from
    shelfLocation = (
        homeDir + "mayaScripts/prefs/shelf/shelf_AnD_CGI.mel"
    )
    if os.path.isdir(shelfLocation) and not cmds.about(batch=True):
        for s in os.listdir(shelfLocation):
            path = os.path.join(shelfLocation, s).replace("\\", "/")
            if not os.path.isfile(path):
                continue
            name = os.path.splitext(s)[0].replace("shelf_", "")
            # Delete existing shelf before loading
            if cmds.shelfLayout(name, ex=1):
                cmds.deleteUI(name)
            mel.eval('loadNewShelf("{}")'.format(path))


# NOTE: Actual setup must be evaluated deferred to avoid

# IOError: [Errno 9]
cmds.evalDeferred(load)
