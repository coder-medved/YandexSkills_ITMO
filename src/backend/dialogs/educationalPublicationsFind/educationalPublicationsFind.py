from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isInContext(event, 'educationalPublications')


educationalPublicationsFind = {'getResponse': getResponse, 'isTriggered': isTriggered}