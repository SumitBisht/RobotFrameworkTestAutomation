import common
from logger import *
from sikuli.Sikuli import Region as SikuliRegion
from sikuli.Sikuli import Screen as SikuliScreen

log = RobotLogger()
class VerifyException(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True
# TODO: appropriately provide for setShowActions(True) 
# NOTE: following commented to resolve problem 'in slow mode - start menu item click fails'
## enable slow motion if debug log level enabled
## (cfgLoggingLevel is set in file common.py)
#if common.cfgLoggingLevel.lower() == 'debug':
#    setShowActions(True)

# =============================================== #
#          Overwritten sikuli methods             #
# =============================================== #

# function for calling native sikuli methods
def sikuli_method(name, *args, **kwargs):
    return sys.modules['sikuli.Sikuli'].__dict__[name](*args, **kwargs)

# overwritten Screen.exists method
def exists(target, timeout=0):
    addFoundImage(getFilename(target))
    return sikuli_method('exists', target, float(timeout))

'''
The verify method acts as a semantic wrapper over the exists method.
On a failure, the log is generated while specifying the non-existence of images to be verified,
but no error is reported and the tests run uninterrupted. 
'''
def verify(target, timeout=0):
    addFoundImage(getFilename(target))
    result = sikuli_method('exists', target, float(timeout))
    if not result:
        log.html_img("verify: Find failed", "images/"+getFilename(target))
        sik_scrn = SikuliScreen()
        log.screenshot(msg="Source Image", region=(sik_scrn.getX(), sik_scrn.getY(), sik_scrn.getW(), sik_scrn.getH()))
        raise VerifyException('Find failed for image ' + getFilename(target))
    return result
#The overwritten click method
def click(target, modifiers=0):
    try:
        return sikuli_method('click', target, modifiers)
    except FindFailed, e:
        log.html_img("click: Find failed", "images/"+getFilename(target))
        sik_scrn = SikuliScreen()
        log.screenshot(msg="Screen", region=(sik_scrn.getX(), sik_scrn.getY(), sik_scrn.getW(), sik_scrn.getH()))
        raise e

def doubleClick(target, modifiers=0):
    try:
        return sikuli_method('doubleClick', target, modifiers)
    except FindFailed, e:
        log.html_img("doubleClick: Find failed", "images/"+getFilename(target))
        sik_scrn = SikuliScreen()
        log.screenshot(msg="Screen", region=(sik_scrn.getX(), sik_scrn.getY(), sik_scrn.getW(), sik_scrn.getH()))
        raise e

def rightClick(target, modifiers=0):
    try:
        return sikuli_method('rightClick', target, modifiers)
    except FindFailed, e:
        log.html_img("rightClick: Find failed", "images/"+getFilename(target))
        sik_scrn = SikuliScreen()
        log.screenshot(msg="Screen", region=(sik_scrn.getX(), sik_scrn.getY(), sik_scrn.getW(), sik_scrn.getH()))
        raise e

def wait(target, timeout=4):
    try:
        return sikuli_method('wait', target, float(timeout))
    except FindFailed, e:
        log.html_img("wait: Find failed", "images/"+getFilename(target))
        sik_scrn = SikuliScreen()
        log.screenshot(msg="Screen", region=(sik_scrn.getX(), sik_scrn.getY(), sik_scrn.getW(), sik_scrn.getH()))
        raise e


# =============================================== #
#          Overwritten sikuli classes             #
# =============================================== #

# overwriten Sikuli Region class
class Region(SikuliRegion, BaseLogger):

    def click(self, target, modifiers=0):
        try:
            return SikuliRegion.click(self, target, modifiers)
        except FindFailed, e:
            self.log.html_img("region.click: Find failed", "images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e

    def doubleClick(self, target, modifiers=0):
        try:
            return SikuliRegion.doubleClick(self, target, modifiers)
        except FindFailed, e:
            self.log.html_img("region.doubleClick: Find failed", "images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e
    def exists(self, target, timeout=None):
        img = getFilename(target)
        reg = (self.getX(), self.getY(), self.getW(), self.getH())
        addFoundImage(img, reg)
        return SikuliRegion.exists(self, target, timeout)
    
    def verify(self, target, timeout=None):
        img = getFilename(target)
        reg = (self.getX(), self.getY(), self.getW(), self.getH())
        addFoundImage(img, reg)
        return SikuliRegion.exists(self, target, timeout)
