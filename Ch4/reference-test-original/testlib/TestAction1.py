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
        type("this is a reference test example")
        wait(0.485)
        None
