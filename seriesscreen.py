from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ListProperty,StringProperty
from library import getPages
from os.path import join
from imageviewscreen import ImageViewScreen
from kivy.core.window import Window

class ChapterLabel(Label):
    chapterindex = 0
    basepath = ""
    chapters = []
    myRootScreenManager = None
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            myImageViewScreen = ImageViewScreen(basepath=self.basepath,chapters=self.chapters,chapterindex=self.chapterindex)
            self.myRootScreenManager.switch_to(myImageViewScreen)
            #maximize window for better readability. TODO remember to minimize on exit
            Window.maximize()
class SeriesScreen(Screen):
    chapters = ListProperty() #list of chapter names; expected to be natural sorted
    basepath = StringProperty() #path to the series folder
    myRootScreenManager = None
    def on_chapters(self,instance,value):
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
