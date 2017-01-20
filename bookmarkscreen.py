from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from library import getChapters
import pickle
from kivy.properties import ListProperty

FILENAME_PKL = 'mangahub.pkl'

def getBookmarks():
    '''
    Reads pkl for list of bookmarks and returns an array with items
    of the form (desc,basepath,chapterindex,pageindex). Returns empty array
    if no bookmarks found.
    '''
    pkl_read = open(FILENAME_PKL,'rb')
    current_dict = pickle.load(pkl_read)
    pkl_read.close()
    try:
        return current_dict['bookmarks']
    except KeyError:
        return []

def addBookmark(desc,basepath,chapterindex,pageindex):
    '''
    Adds the tuple (desc, basepath, chapterindex, pageindex) to the array
    present in pkl['bookmarks'].
    '''
    # pkl must exist since sources added
    pkl_read = open(FILENAME_PKL,'rb')
    current_dict = pickle.load(pkl_read)
    pkl_read.close()
    if 'bookmarks' in current_dict:
        current_dict['bookmarks'].append((desc,basepath,chapterindex,pageindex))
    else:
        # no key 'bookmarks' exists
        current_dict['bookmarks'] = [(desc,basepath,chapterindex,pageindex)]
    pkl_write = open(FILENAME_PKL,'wb')
    pickle.dump(current_dict,pkl_write)
    pkl_write.close()

class LblRow(BoxLayout):
    '''
    Custom widget defining a single row of data displayed on the BookmarkScreen.
    '''
    textvalues = ListProperty(['','','',''])
    bookmark_data = ListProperty()
    myRootScreenManager = None

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.myRootScreenManager.openImageScreen(*self.extractBookmarkData(self.bookmark_data))
    def extractBookmarkData(self,bkmrk):
        # bkmrk = (desc, basepath,chapterindex,pageindex)
        chapters = getChapters(bkmrk[1])
        return (bkmrk[1],chapters,bkmrk[2],bkmrk[3])

class BookmarkScreen(Screen):
    '''
    Screen widget that holds other widgets and is added to ScreenManager.
    Contains a GridLayout that displays all Bookmarks.
    '''
    bookmarks = ListProperty()
    myRootScreenManager = None

    def __init__(self,rootscreenmanager,**kwargs):
        super(BookmarkScreen,self).__init__(**kwargs)
        self.myRootScreenManager = rootscreenmanager
        self.bookmarks = getBookmarks()
        self._keyboard = Window.request_keyboard(self._keyboard_closed,self)
        self._keyboard.bind(on_key_down = self.on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None

    def on_keyboard_down(self,keyboard,keycode,text,modifiers):
        if keycode[1]=='backspace':
            self.myRootScreenManager.returnToHome()
            return True

    def on_bookmarks(self,instance,value):
        layout = self.ids.layout_grid
        layout.clear_widgets()
        serial = 1
        for bkmrk in value:
            row = LblRow()
            row.textvalues = ['#'+str(serial),bkmrk[0],'Chapter '+str(bkmrk[2]+1),'Page '+str(bkmrk[3]+1)]
            row.bookmark_data = bkmrk
            row.myRootScreenManager = self.myRootScreenManager
            layout.add_widget(row)
            serial += 1

class BookmarkPopupContent(GridLayout):
    '''
    Layout widget which is the root widget for the 'Add Bookmark' Popup.
    '''
    pass
