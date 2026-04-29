# Maya Scripts

This repository is a collection of Autodesk Maya shelf tools created by AnD CGI
to automate small production tasks, speed up common scene operations, and fill
workflow gaps in Maya.

## Project Status

This repository is in final-maintenance mode. The scripts have been refreshed
for a final Maya 2027/Python 3 compatibility pass, but the project is no longer
intended to receive ongoing feature work after the final archival release.

Use these tools at your own risk. Some scripts were originally written for
specific studio pipelines and may need local configuration before they make
sense in another environment.

## Compatibility

- Target: Autodesk Maya 2027 or newer Maya builds that run Python 3.
- Older Maya/Python 2 releases are no longer a goal for this repo.
- The tools use `maya.cmds` and MEL shelf commands, so they must run inside Maya.
- A few tools depend on optional renderer features, such as Arnold `aiAOV`
  nodes.

## Install

### 🔹 Auto-load Installation
Download from the release page:  
👉 [Download Release v1.0.1](https://github.com/AnDCGI/AnD_mayaScripts/releases/tag/v1.0.1)

### 🔹 Manual Installation
Follow the steps below.

1. Keep this repository somewhere stable, for example:

   ```text
   C:/Users/<USER>/Documents/GitHub/AnD_mayaScripts
   ```

2. In Maya, open the Script Editor, switch to the Python tab, and run:

   ```python
   import os
   import sys

   repo = r"C:\Users\<USER>\Documents\GitHub\AnD_mayaScripts"
   os.environ["AND_MAYA_REPO_ROOT"] = repo
   sys.path.insert(0, repo + r"\scripts")

   import userSetup
   userSetup.load()
   ```

3. Maya should load the `AnDCGI` shelf from `prefs/shelf/shelf_AnDCGI.mel`.

For automatic loading on every Maya start, create or edit this file:

```text
~/Documents/maya/2027/scripts/userSetup.py
```

and put this bootstrap in it:

```python
import os
import sys

repo = r"C:\Users\<USER>\Documents\GitHub\AnD_mayaScripts"
os.environ["AND_MAYA_REPO_ROOT"] = repo
sys.path.insert(0, repo + r"\scripts")

import userSetup
userSetup.load()
```

The startup loader adds the nested `scripts/py-scripts` folders to `sys.path`
and adds the repository `icons` folder to Maya's icon lookup path.
Replace `<USER>` with your Windows account name in the examples above.

## Optional Configuration

Some legacy production scripts used hardcoded studio paths. They now read
optional settings from:

```text
~/Documents/AnD_mayaScripts/config.json
```

Use `config.sample.json` as a starting point. Environment variables with the
`AND_MAYA_` prefix also work, for example `AND_MAYA_SAVE_SCENE_ROOT`.

## Tool Index

| Tool | File | Purpose |
| --- | --- | --- |
| Arnold Delete AOV | `scripts/py-scripts/ai_MtoA/aiDeleteAOV.py` | Imports references and removes Arnold AOV nodes. |
| Arnold Disable AOV | `scripts/py-scripts/ai_MtoA/aiDisableAOV.py` | Disables all Arnold AOV nodes in the scene. |
| Arnold Matte | `scripts/py-scripts/ai_MtoA/aiMatte.py` | Enables `aiMatte` on supported shape nodes. |
| Channel Copy/Paste | `scripts/py-scripts/channelCopyPaste/hfCopyPaste.py` | Copies highlighted channel box values and pastes them onto selected objects. |
| Clean Namespace | `scripts/py-scripts/cleanNameSpace/cleanNameSpace.py` | Merges non-default namespaces back to root. |
| Clean Unknown Plugins | `scripts/py-scripts/cleanUnknwonPlugins/cleanUnknwonPlugins.py` | Removes unknown nodes, unknown plugins, and `_UNKNOWN_REF_NODE_`. |
| Dynamics Quick Selection Set | `scripts/py-scripts/dynamicsQuickSelectionSet/dynamicsQuickSelectionSet.py` | Builds quick selection sets for FX/dynamics node types. |
| Fancy Separator | `scripts/py-scripts/fancySeparator/fancySeparator.py` | Adds colored or custom icon separators to the active Maya shelf. |
| Channel Box Speed | `scripts/py-scripts/helperTools/channelBoxSpeed.py` | Adds a HUD slider for channel box drag speed. |
| Batch Render Script | `scripts/py-scripts/mayaBatchRenderScript/batchRenderScript.py` | Appends the current scene to a daily batch render `.bat` file. |
| Save Scene | `scripts/py-scripts/mayaSaveScene/mayaSaveScene.py` | Saves a versioned Maya ASCII scene using configurable paths. |
| Scene Scale | `scripts/py-scripts/mayaSceneScale/mayaSceneScaleChange.py` | Parents scene assemblies under a `sceneScale` locator with a global scale attribute. |
| Reference Checker | `scripts/py-scripts/referenceFix/referenceList.py` | Scans Maya ASCII files for references outside the expected root. |
| Render-Time Catmull-Clark | `scripts/py-scripts/render-TimeCatmull-ClarkSubdivision/RTCatClark.py` | Temporarily smooths previewed meshes during render and restores them after. |
| Rivet Constraint | `scripts/py-scripts/rivetConstraint/rivetConstraint.py` | Creates a rivet locator from selected mesh edges or surface points. |
| FPS Switch | `scripts/py-scripts/switchFPS/mayaBroadcastFPS.py` | Sets Maya FPS and playback range from a small UI. |
| Support Links | `scripts/py-scripts/helpSupport/*.py` | Opens GitHub and Gumroad support links from Maya. |

## Render-Time Catmull-Clark Usage

Add these snippets in Render Settings > Common > Render Options:

```mel
Pre Render MEL = python("import RTCatClark;RTCatClark.preCatClark()")
Post Render MEL = python("import RTCatClark;RTCatClark.pstCatClark()")
```

## Known Limitations

- These are shelf scripts, not a packaged Maya module.
- Some tools operate directly on the open scene and are intentionally
  destructive, such as namespace cleanup and unknown plugin cleanup.
- The shelf preserves legacy module names and folder names, including historical
  typos, to avoid breaking launch commands.
- Compatibility has been checked statically outside Maya, but final behavior
  should be tested inside Maya before publishing the archive release.

## License

Except where otherwise noted, this project is licensed under the Creative
Commons Attribution-ShareAlike 4.0 International License. See `LICENSE.md`.
