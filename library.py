from os import listdir
import pickle

FILENAME_PKL = "mangahub.pkl"

def addSource(sourcepath):
    '''
    Adds this directory as one of the sources for the library
    '''
    current_dict={'sources':[]}
    try:
        pkl_read = open(FILENAME_PKL,'rb')
        current_dict = pickle.load(pkl_read)
        pkl_read.close()
    except:
        #pkl doesn't exist
        pass
    current_dict['sources'].append(sourcepath)
    pkl_write = open(FILENAME_PKL,'wb')
    pickle.dump(current_dict,pkl_write)
    pkl_write.close()

def getSources():
    '''
    Returns all sources as a list
    '''
    try:
        pkl_read = open(FILENAME_PKL,'rb')
        return pickle.load(pkl_read)['sources']
    except:
        return []
    
def getSeries(sourcepath):
    '''
    Returns a list of string Series titles found in the source directory passed
    '''
    return listdir(sourcepath)
def getAllSeries():
    '''
    Returns a list containing series from all sources
    '''
    allseries=[]
    for source in getSources():
        allseries = allseries + getSeries(source)
    return allseries
