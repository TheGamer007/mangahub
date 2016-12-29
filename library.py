from os import listdir

def addSource(sourcepath):
    '''
    Adds this directory as one of the sources for the library
    '''
    #Store in pkl as an element of a list of paths, which is dict value

def getSources():
    '''
    Lists all the directories which are sources for the library
    '''
    #Read the pkl dict and display all elems of list
    
def getSeries(sourcepath):
    '''
    Returns all series in the source directory passed as a list of strings
    '''
    return listdir(sourcepath)
