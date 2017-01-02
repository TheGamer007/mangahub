from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty
from kivy.uix.label import Label
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

def removeSource(sourcepath):
    '''
    Removes the passed source, if in sources
    '''
    current_dict = {'sources':[]}
    try:
        pkl_read = open(FILENAME_PKL,'rb')
        current_dict = pickle.load(pkl_read)
        pkl_read.close()
        current_dict['sources'].remove(sourcepath)
    except ValueError:
        print 'No such source exists'
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

class SourcesDialogLabel(Label):
    pass

class SourcesDialogContent(AnchorLayout):
    titles = ListProperty()
    def getSources(self):
        return getSources()
    def buttonPressed(self,button):
        #TODO Provide filechooser for path selection
        new_source = 'F:\\Pokemon Games'
        #TODO add to sources, then to titles
        addSource(new_source)
        self.titles.append(new_source)
    def on_titles(self,instance,values):
        sources = self.ids['current_sources']
        #remove old labels
        sources.clear_widgets()
        #add from new sources list
        for source in values:
            item = SourcesDialogLabel()
            item.text = source
            sources.add_widget(item)
        sources.add_widget(Label())
