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
        type("5 ")
        wait(0.547)
        type("4 ")
        wait(0.391)
        type("3 ")
        wait(0.368)
        type("2 ")
        wait(0.368)
        type("1 ")
        wait(0.357)
        type("0 ")
        wait(1)
        type(" boom")
        wait(0.546)
        None
