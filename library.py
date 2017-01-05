from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.garden.FileBrowser import FileBrowser
from kivy.uix.popup import Popup
from os import listdir
from os.path import isdir, join
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
    #TODO listdir is unsorted, natural sort before return
    return listdir(sourcepath)
def getAllSeries():
    '''
    Returns a list containing tuples of the form (source_path,series_name)
    '''
    allseries=[]
    for source in getSources():
        allseries = allseries + map(lambda x: (source,x),getSeries(source))
    return allseries
def getChapters(seriespath):
    '''
    Returns the directories in passed path.
    These correspond to chapters of the series
    '''
    #TODO natural sort before return
    return listdir(seriespath)
def getPages(chapterpath):
    '''
    Returns all files in the passed path.
    These correspond to pages of the chapter
    '''
    #TODO natural sort before return
    return listdir(chapterpath)
class SourcesDialogLabel(Label):
    pass

class SourcesDialogContent(AnchorLayout):
    titles = ListProperty()
    def getSources(self):
        return getSources()
    def buttonPressed(self,button):
        browser = FileBrowser(select_string='Select Source')
        browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled)
        browser.dirselect= True
        browser.filters = [self.is_dir]
        pop = Popup(title='FileBro',content=browser)
        pop.open()
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
    def is_dir(self,directory,filename):
        return isdir(join(directory,filename))
    def _fbrowser_canceled(self, instance):
        #close the FileBrowser Popup
        instance.parent.parent.parent.dismiss()
    def _fbrowser_success(self, instance):
        # add the selection to sources
        new_source = instance.selection[0]
        addSource(new_source)
        self.titles.append(new_source)
        # now close the FileBrowser Popup
        instance.parent.parent.parent.dismiss()
