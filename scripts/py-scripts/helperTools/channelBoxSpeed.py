"""Add a temporary HUD slider for Maya channel box drag speed."""

import maya.cmds as cmds


def SliderSpeed(hud, *args):
    """Update the channel box speed and optionally remove the HUD."""
    try:
        sliderValue = cmds.hudSliderButton(hud, query=True, v=True)
        newSpeed = pow(10, sliderValue)
        cmds.channelBox("mainChannelBox", edit=True, spd=newSpeed)
        if newSpeed < 1.0:
            newSpeed = "%.6f" % newSpeed
        else:
            newSpeed = int(newSpeed)
        cmds.hudSliderButton(hud, e=True, sl=newSpeed)
    except RuntimeError:
        print("channelBox not existed.")
    if args and args[0] == 'delete':
        cmds.headsUpDisplay(hud, rem=True)


# Create the HUD immediately because this tool is meant to be shelf-launched.
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
