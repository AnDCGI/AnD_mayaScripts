import maya.cmds as cmds
import maya.mel as mel
import re

def rivet():
    messageOne = "Please Select Two Edges"
    messageTwo = "Select Two Edges"
    nameObject = ""
    namePOSI = ""
    parts = []
    edgeList = cmds.filterExpand(sm = 32)
    
    if edgeList != None:
        size = len(edgeList)
        if size > 0:
            if size != 2:
                cmds.error(messageOne)
                return ""
                			
        parts = edgeList[0].split(".")
        nameObject = parts[0]
        edgeOne = re.findall("\d+", parts[1])
        edgeOne = float(edgeOne[0])
        parts = edgeList[1].split(".")
        edgeTwo = re.findall("\d+", parts[1])
        edgeTwo = float(edgeTwo[0])
        nameCFMEOne = str(cmds.createNode('curveFromMeshEdge', n="rivetCurveFromMeshEdge1"))
        cmds.setAttr(".ihi", 1)
        cmds.setAttr(".ei[0]", edgeOne)
        nameCFMETwo = str(cmds.createNode('curveFromMeshEdge', n="rivetCurveFromMeshEdge2"))
        cmds.setAttr(".ihi", 1)
        cmds.setAttr(".ei[0]", edgeTwo)
        nameLoft = str(cmds.createNode('loft', n="rivetLoft1"))
        cmds.setAttr(".ic", s=2)
        cmds.setAttr(".u", True)
        cmds.setAttr(".rsn", True)
        namePOSI = str(cmds.createNode('pointOnSurfaceInfo', n="rivetPointOnSurfaceInfo1"))
        cmds.setAttr(".turnOnPercentage", 1)
        cmds.setAttr(".parameterU", 0.5)
        cmds.setAttr(".parameterV", 0.5)
        cmds.connectAttr((nameLoft + ".os"), (namePOSI + ".is"), f=1)
        cmds.connectAttr((nameCFMEOne + ".oc"), (nameLoft + ".ic[0]"))
        cmds.connectAttr((nameCFMETwo + ".oc"), (nameLoft + ".ic[1]"))
        cmds.connectAttr((nameObject + ".w"), (nameCFMEOne + ".im"))
        cmds.connectAttr((nameObject + ".w"), (nameCFMETwo + ".im"))
        		
    else:
        edgeList = cmds.filterExpand(sm=41)
        size = len(edgeList)
        if size > 0:
            if size != 1:
                cmds.error("No One Point Selected")
                return ""
				
            parts = edgeList[0].split(".")
            nameObject = parts[0]
            parts = edgeListmx[0].split("[]")
            u = float(parts[1])
            v = float(parts[2])
            namePOSI = str(cmds.createNode('pointOnSurfaceInfo', n="rivetPointOnSurfaceInfo1"))
            cmds.setAttr(".turnOnPercentage", 0)
            cmds.setAttr(".parameterU", u)
            cmds.setAttr(".parameterV", v)
            cmds.connectAttr((nameObject + ".ws"), (namePOSI + ".is"), f=1)
			
		
        else:
            cmds.error("No Edges or Point Selected")
            return ""
			
		
    nameLocator = str(cmds.createNode('transform', n = "rivetOrient_1"))
    cmds.createNode('locator', p = nameLocator, n =(nameLocator + "Shape"))
    nameAC = str(cmds.createNode('aimConstraint', p = nameLocator, n =(nameLocator + "_rivetAimConstraint_1")))
    cmds.setAttr(".tg[0].tw", 1)
    cmds.setAttr(".a", 0, 1, 0, type="double3")
    cmds.setAttr(".u", 0, 0, 1, type="double3")
    cmds.setAttr(".v", k = False)
    cmds.setAttr(".tx", k = False)
    cmds.setAttr(".ty", k = False)
    cmds.setAttr(".tz", k = False)
    cmds.setAttr(".rx", k = False)
    cmds.setAttr(".ry", k = False)
    cmds.setAttr(".rz", k = False)
    cmds.setAttr(".sx", k = False)
    cmds.setAttr(".sy", k = False)
    cmds.setAttr(".sz", k = False)
    cmds.setAttr((nameLocator + ".useOutlinerColor"), 1)
    cmds.setAttr((nameLocator + ".outlinerColor"), 0, 1, 0)
    cmds.setAttr((nameLocator + ".overrideEnabled"), 1)
    cmds.setAttr((nameLocator + ".overrideColor"), 13)
    cmds.connectAttr((namePOSI + ".position"), (nameLocator + ".translate"))
    cmds.connectAttr((namePOSI + ".n"), (nameAC + ".tg[0].tt"))
    cmds.connectAttr((namePOSI + ".tv"), (nameAC + ".wu"))
    cmds.connectAttr((nameAC + ".crx"), (nameLocator + ".rx"))
    cmds.connectAttr((nameAC + ".cry"), (nameLocator + ".ry"))
    cmds.connectAttr((nameAC + ".crz"), (nameLocator + ".rz"))
    cmds.select(nameLocator, r = 1)
    return (nameLocator)
    mel.eval('AEdagNodeCommonRefreshOutliners()')
    mel.eval('AttributeEditor;updateAE()')
	
rivet()
