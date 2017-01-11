from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from os.path import isdir, join
import pickle
from kivy.properties import ListProperty

FILENAME_PKL = 'mangahub.pkl'

def getBookmarks():
    # read from pkl['bookmarks'] = [(),(desc,basepath,chapterindex,pageindex),()]
    pkl_read = open(FILENAME_PKL,'rb')
    current_dict = pickle.load(pkl_read)
    pkl_read.close()
    try:
        return current_dict['bookmarks']
    except KeyError:
        return []

def addBookmark(desc,basepath,chapterindex,pageindex):
    # add to pkl['bookmarks'] = (desc, basepath, chapterindex, pageindex)
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

class BookmarkScreen(Screen):
    bookmarks = ListProperty()
    myRootScreenManager = None

    def __init__(self,**kwargs):
        super(BookmarkScreen,self).__init__(**kwargs)
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
            print bkmrk
            layout.add_widget(Label(text='#'+str(serial),size_hint=(None,None),color=[0,0,0,1]))
            layout.add_widget(Label(text=bkmrk[0],size_hint=(1,None),color=[0,0,0,1]))
            layout.add_widget(Label(text='Chapter '+str(bkmrk[2]+1),size_hint=(None,None),color=[0,0,0,1]))
            layout.add_widget(Label(text='Page '+str(bkmrk[3]+1),size_hint=(None,None),color=[0,0,0,1]))
            serial += 1

class BookmarkPopup(GridLayout):
    pass
