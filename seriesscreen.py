from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ListProperty,StringProperty
from library import getPages
from os.path import join
from imageviewscreen import ImageViewScreen
from kivy.core.window import Window

class ChapterLabel(Label):
    chapterpath = StringProperty()
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            pagelist = map(lambda x: join(self.chapterpath,x), getPages(self.chapterpath))
            myRootScreenManager = self.parent.parent.parent.parent.parent
            myImageViewScreen = ImageViewScreen(pages=pagelist)
            myRootScreenManager.switch_to(myImageViewScreen)
            #maximize window for better readability. TODO remember to minimize on exit
            Window.maximize()
class SeriesScreen(Screen):
    chapters = ListProperty() #list of chapter names; expected to be natural sorted
    basepath = StringProperty() #path to the series folder

    def on_chapters(self,instance,value):
        chapterslist = self.ids.chapters_list
        #remove old labels
        chapterslist.clear_widgets()
        #add new labels
        for chapter in value:
            item = ChapterLabel()
            item.text = chapter
            item.chapterpath = join(self.basepath,chapter)
            chapterslist.add_widget(item)
