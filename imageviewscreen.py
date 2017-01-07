from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.label import Label
from os.path import join
from library import getPages

class ImageViewScreen(Screen):
    '''
    Topmost widget that encompasses all buttons and
    an image screenmanager for displaying images
    '''
    myScreenManager = None
    pageslist = [] #this is expected to be a natural sorted list of paths to the images
    chapterslist = [] # natsorted list of chapters
    pageindex, chapterindex = 0,0
    basepath = ""

    def __init__(self,chapters,chapterindex,basepath,**kwargs):
        super(ImageViewScreen,self).__init__(**kwargs)
        self.myScreenManager = self.ids.images_manager
        self.basepath = basepath
        self.chapterslist = chapters
        self.chapterindex = chapterindex
        chapterpath = join(self.basepath,self.chapterslist[self.chapterindex])
        self.pageslist = map(lambda x: join(chapterpath,x), getPages(chapterpath))
        self.myScreenManager.switch_to(ImageScreen(src = self.pageslist[self.pageindex]))
        self._keyboard = Window.request_keyboard(self._keyboard_closed,self)
        self._keyboard.bind(on_key_down = self.on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None

    def on_keyboard_down(self,keyboard,keycode,text,modifiers):
        # keycode is a tuple of the form (int,str)
        # key pressed as str is therefore == keycode[1]
        if keycode[1]=='left' or keycode[1]=='a':
            self.prevPage()
        elif keycode[1]=='right' or keycode[1]=='d':
            self.nextPage()

    def prevPage(self):
        if self.pageindex == 0:
            # first page in chapter, jump to previous
            self.prevChapter(None)
        else:
            self.pageindex -= 1
            imgscreen = ImageScreen(src = self.pageslist[self.pageindex])
            self.myScreenManager.switch_to(imgscreen,direction='right')

    def nextPage(self):
        if self.pageindex == (len(self.pageslist)-1):
            # last page in chapter, jump to next
            self.nextChapter(None)
        else:
            self.pageindex += 1
            imgscreen = ImageScreen(src = self.pageslist[self.pageindex])
            self.myScreenManager.switch_to(imgscreen,direction='left')

    def prevChapter(self,button):
        if self.chapterindex == 0:
            # no chapter before this, give alert
            p = Popup(title="Alert",content=Label(text="You have reached the first page of the first chapter!"),size_hint=(0.4,0.4))
            p.open()
        else:
            # jump to previous chapter
            self.chapterindex -= 1
            chapterpath = join(self.basepath,self.chapterslist[self.chapterindex])
            self.pageslist = map(lambda x: join(chapterpath,x), getPages(chapterpath))
            # last page of prev if using keys, first page if button
            if button != None:
                self.pageindex = 0
            else:
                self.pageindex = len(self.pageslist) - 1
            imgscreen = ImageScreen(src = self.pageslist[self.pageindex])
            self.myScreenManager.switch_to(imgscreen,direction='right')

    def nextChapter(self,button):
        if self.chapterindex == (len(self.chapterslist)-1):
            # no chapter after this, give alert
            p = Popup(title="Alert",content=Label(text="You have reached the last page of the last chapter!"),size_hint=(0.4,0.4))
            p.open()
        else:
            # jump to next chapter.
            # Doesn't matter by key or button, go to first page
            self.chapterindex += 1
            chapterpath = join(self.basepath,self.chapterslist[self.chapterindex])
            self.pageslist = map(lambda x: join(chapterpath,x), getPages(chapterpath))
            self.pageindex = 0
            imgscreen = ImageScreen(src = self.pageslist[self.pageindex])
            self.myScreenManager.switch_to(imgscreen,direction='left')

class ImageScreen(Screen):
    '''
    Screen consisting of only one Image widget
    '''
    src = StringProperty() #This src corresponds to the image file
