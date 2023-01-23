import maya.cmds as cmds

version = 1.0
winID = 'SetDesiredFPS'

fps_options = {'Game 15 FPS': 15, 'Film 24 FPS': 24, 'PAL/SECAM 25 FPS': 25, 'NTSC 30 FPS': 30}

if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)


def set_fps(*args):
    current_value = cmds.optionMenu('Select_FPS', query=True, value=True)
    start_time = cmds.intField('strtFrame', query=True, value=True)
    end_time = cmds.intField('endFrame', query=True, value=True)

    fps = fps_options[current_value]
    cmds.currentUnit(time=current_value.split()[0].lower())
    cmds.playbackOptions(ps=0, e=True, ast=start_time, aet=end_time)
    cmds.playButtonStart()
    cmds.inViewMessage(amg=f'Changed FPS to <hl>{fps}</hl>', pos='midCenter', fade=True)
    cmds.window(winID, title='Set Desired FPS', widthHeight=(200, 150))
    cmds.columnLayout()

    cmds.frameLayout(label='Select FPS')
    cmds.optionMenu('Select_FPS', label='FPS')
    for option in fps_options:
        cmds.menuItem(label=option)
    cmds.setParent('..')

    cmds.frameLayout(label='Animation Range')
    cmds.rowLayout(numberOfColumns=2)
    cmds.text(label='Start Frame:')
    cmds.intField('strtFrame', minValue=1, value=101)
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=2)
    cmds.text(label='End Frame:')
    cmds.intField('endFrame', minValue=1, value=500)
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.separator(style='none')

    cmds.button(label='Set FPS', command=set_fps)

    cmds.showWindow(winID)
