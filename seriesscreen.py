from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ListProperty,StringProperty
from imageviewscreen import ImageViewScreen
from kivy.core.window import Window

class ChapterLabel(Label):
    '''
    Custom Label implementation that displays each chapter name.
    '''
    chapterindex = 0
    basepath = ""
    chapters = []
    myRootScreenManager = None
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            myImageViewScreen = ImageViewScreen(basepath=self.basepath,chapters=self.chapters,chapterindex=self.chapterindex)
            myImageViewScreen.myRootScreenManager = self.myRootScreenManager
            self.myRootScreenManager.switch_to(myImageViewScreen)
            # maximize window for better readability.
            Window.maximize()
class SeriesScreen(Screen):
    '''
    Screen widget that holds other widgets and is added to ScreenManager.
    Contains a Label with the series name, and a ScrollView that displays the chapters.
    '''
    chapters = ListProperty() #list of chapter names; expected to be natural sorted
    basepath = StringProperty() #path to the series folder
    myRootScreenManager = None

    def __init__(self,**kwargs):
        super(SeriesScreen,self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed,self)
        self._keyboard.bind(on_key_down = self.on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None

    def on_keyboard_down(self,keyboard,keycode,text,modifiers):
        if keycode[1]=='backspace':
            self.myRootScreenManager.returnToHome()
            return True

    def on_chapters(self,instance,value):
        '''
        Kivy event callback calls this method everytime the 'chapters' list variable is modified.
        '''
        chapterslist = self.ids.chapters_list
        #remove old labels
        chapterslist.clear_widgets()
        #add new labels
        index = 0
        for chapter in value:
            item = ChapterLabel()
            item.text = chapter
            item.chapterindex = index
            item.chapters = self.chapters
            item.basepath = self.basepath
            item.myRootScreenManager = self.myRootScreenManager
            chapterslist.add_widget(item)
            index += 1
