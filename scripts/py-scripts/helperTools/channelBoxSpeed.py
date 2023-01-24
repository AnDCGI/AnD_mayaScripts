import maya.cmds as cmds
from math import log10


def SliderSpeed(hud, *args):
    """
    This function modifies the speed of the mainChannelBox based on the value of the hudSliderButton.
    :param hud: hudSliderButton name
    :param args: 'delete' option
    """
    try:
        sliderValue = cmds.hudSliderButton(hud, query=True, v=True)
        newSpeed = pow(10, sliderValue)
        cmds.channelBox("mainChannelBox", edit=True, spd=newSpeed)
        if newSpeed < 1.0:
            newSpeed = "%.6f" % newSpeed
        else:
            newSpeed = int(newSpeed)
        cmds.hudSliderButton(hud, e=True, sl=newSpeed)
    except:
        print("channelBox not existed.")
    if len(args) > 0:
        if args[0] == 'delete':
            cmds.headsUpDisplay(hud, rem=True)


sliderSpeedValue = cmds.channelBox("mainChannelBox", query=True, spd=1)
hud = cmds.hudSliderButton('HUDchboxspeed',
                           section=2,
                           block=5,
                           visible=True,
                           sliderLabel='Speed',
                           value=0,
                           type='int',
                           minValue=-6,
                           maxValue=6,
                           sliderLabelWidth=50,
                           valueWidth=50,
                           sliderLength=100,
                           sliderIncrement=1,
                           buttonLabel='Reset & Delete',
                           buttonWidth=100,
                           buttonShape='rectangle',
                           buttonReleaseCommand=lambda: SliderSpeed('HUDchboxspeed', 'delete'),
                           sliderDragCommand=lambda: SliderSpeed('HUDchboxspeed'))
