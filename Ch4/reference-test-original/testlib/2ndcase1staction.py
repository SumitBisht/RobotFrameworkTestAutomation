from __future__ import with_statement
from sikuliwrapper import *

#add custom image library
addImagePath(common.cfgImageLibrary)
Settings.MinSimilarity = common.imageMinSimilarity

class XTest(BaseLogger):
    
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self):
        None
        #self.appCoordinates = (0, 0, 1024, 768)

    def Execute(self, *args):
        keyDown(Key.ENTER)
        keyUp(Key.ENTER)
        wait(1.156)
        type("case changed")
        wait(0.907)
        None
