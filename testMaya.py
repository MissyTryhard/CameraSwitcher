from maya import OpenMayaUI as omui
from PySide.QtCore import * 
from PySide.QtGui import * 
from shiboken import wrapInstance 

omui.MQtUtil.mainWindow()    
ptr = omui.MQtUtil.mainWindow()    
widget = wrapInstance(long(ptr), QWidget)