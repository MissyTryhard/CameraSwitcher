import maya.cmds as mc
import os
import re
from functools import partial

'''
public Vars
'''
newPath = r'/Users/Lopakka/Documents/Py4Maya/TestFolder/'
btnListNames = []
cameras = mc.ls(type=('camera'), sn=True)
startupCams = [camera for camera in cameras if mc.camera(mc.listRelatives(camera, parent=True)[0], startupCamera=True, q=True)]
nonDefCams = list(set(cameras) - set(startupCams))
nonDefCams.sort()
currentSelectedCam = ''


'''
Methods
'''
#populates buttonList
def ListWithButtons():   
    for item in nonDefCams:
        #firstSymbPos = item.find('|')
        #lastSymbPos = item.rfind('|')        
        for i in range(len(nonDefCams)):
            #item = "Camera_%s"%(chr(i+97))            
            item = nonDefCams[i]
            if item.find("Shape"):
                newItem = item.replace('Shape', '')       
            btnListNames.append(newItem)       
        break
        
def CallBack(value):
    '''
    Returns the button that is pressed in the UI 
    https://stackoverflow.com/questions/37034838/printing-the-label-of-a-button-when-clicked/37038947
    '''
    def inner_callback(_):
        #print value, "was clicked"
        mc.lookThru(nonDefCams[value])       
        #mc.select(nonDefCams[value]) ### is currently selecting the shape node and not the TRS node
        mc.select(re.sub("Shape", "", nonDefCams[value])) # clipping out the "Shape" string cmd.ls is giving
        #selKeys((re.sub("Shape", "", nonDefCams[value])))     
    return inner_callback

'''
def selKeys(val):
    cameraSel = val
    firstKey = mc.findKeyframe(timeSlider=True, which="first")
    lastKey = mc.findKeyframe(timeSlider=True, which="last")
    #mc.selectKey((val), time=(firstKey, lastKey), keyframe=True)
    mc.playblast(startTime = firstKey, endTime=lastKey)
'''

def PutButtonsInUI():   
    ListWithButtons()
    for i in range(len(nonDefCams)):
        #btnList[i] = mc.button(label=str(nonDefCams[i]), c=lambda *_:CamName(str(i)))
        btnListNames[i] = mc.button(label=str(btnListNames[i]), c=CallBack(i))
 


def GrabKey( *args):     
    print(mc.findKeyframe(timeSlider=True, which="first"))
    print(mc.findKeyframe(timeSlider=True, which="last"))
    selection = mc.ls(sl=True)
    #print(mc.ls(sl=True))
    firstKey = mc.findKeyframe(timeSlider=True, which="first")
    lastKey = mc.findKeyframe(timeSlider=True, which="last")
    mc.playblast(startTime = firstKey, endTime=lastKey)
    #mc.selectKey('Camera_A', time=(firstKey, lastKey)) #selects keys but not very well; its hard to pass node name; returns the curves selected in GE

def Refresh(*args):
    '''
    Should refresh the UI and add any new cameras that are added
    to the scene
    '''

def CreateFolders( *args):
    print("value")



def CreateWindow():
    windowID = "MyCustWind"
    if mc.window(windowID, exists=True):
        mc.deleteUI(windowID)        
    mc.window(windowID, title="Kamsies", sizeable=True, resizeToFitChildren=True)
    mc.rowColumnLayout(numberOfColumns=1, columnWidth=[(1,200)])    
    mc.text(label="Camera List")
    PutButtonsInUI()  
    mc.separator( style='none', height=16 )
    grabKeys = mc.button( label="Blasting", c=GrabKey ) ### https://stackoverflow.com/questions/22848582/maya-python-pass-variable-on-button-press#22859613
    refrsh = mc.button( label="Refresh", c=Refresh )

    mc.separator( style='none', height=16 )
    myTextfield = cmds.textField( fi = 'C:\Users\Lopakka\Documents\Py4Maya\TestFolder')
    print(myTextfield)
    createFoldersBut = mc.button(label="Create Folders", c =CreateFolders)

    mc.showWindow(windowID)
    


'''
#Creates separate folders for each camera
for mat in match:
    print(mat)
    try:
        #files = [join(newPath, f) for f in listdir(PATH) if isfile(join(PATH, f))]
        folders = newPath + " " + str(mat)
        os.makedirs(folders)
    except Exception as e:
        print(e.args)
        break   
'''

'''
Main
'''

CreateWindow()