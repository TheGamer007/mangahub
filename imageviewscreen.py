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
    ChapterSpinner, PageSpinner = None, None
    pageslist = []
    pagesFilenames = []
    chapterslist = [] # natsorted list of chapters
    pageindex, chapterindex = 0,0
    basepath = ""
    flag_FromSpinner = True
    myRootScreenManager = None

    def __init__(self,chapters,chapterindex,basepath,**kwargs):
        super(ImageViewScreen,self).__init__(**kwargs)
        self.myScreenManager = self.ids.images_manager
        self.ChapterSpinner = self.ids.spinner_chapter
        self.PageSpinner = self.ids.spinner_page
        self.basepath = basepath
        self.chapterslist = chapters
        self.chapterindex = chapterindex

        chapterpath = join(self.basepath,self.chapterslist[self.chapterindex])
        self.pagesFilenames = getPages(chapterpath)
        self.pageslist = map(lambda x: join(chapterpath,x), self.pagesFilenames)
        self.ChapterSpinner.values = self.chapterslist
        self.PageSpinner.values = self.pagesFilenames
        self.ChapterSpinner.text = self.chapterslist[self.chapterindex]
        self.PageSpinner.text = self.pagesFilenames[self.pageindex]
        self.myScreenManager.switch_to(ImageScreen(src = self.pageslist[self.pageindex]))
        self.ChapterSpinner.bind(text = self.updateChapterSpinner)
        self.PageSpinner.bind(text = self.updatePageSpinner)

        self._keyboard = Window.request_keyboard(self._keyboard_closed,self)
        self._keyboard.bind(on_key_down = self.on_keyboard_down)

    def addBookmark(self,button):
        # add Bookmark Popup here
        pass

    def updateChapterSpinner(self,spinner,text):
        self.chapterindex = spinner.values.index(text)
        chapterpath = join(self.basepath,self.chapterslist[self.chapterindex])
        self.pagesFilenames = getPages(chapterpath)
        self.pageslist = map(lambda x: join(chapterpath,x), self.pagesFilenames)
        if self.flag_FromSpinner:
            self.pageindex = 0
        else:
            self.flag_FromSpinner = True
        # If the user is on page[0] and tries a chapter jump, PageSpinner.text will not be triggered
        # Hence, we pass text as '-1' and substitute in updatePageSpinner
        if self.PageSpinner.text == self.pagesFilenames[self.pageindex]:
            self.PageSpinner.text = ""
        else:
            self.PageSpinner.text = self.pagesFilenames[self.pageindex]

    def updatePageSpinner(self,spinner,text):
        if text == "":
            self.PageSpinner.text = self.pagesFilenames[self.pageindex]
            return # the above change will trigger updatePageSpinner again, so break here
        self.pageindex = spinner.values.index(text)
        imgscreen = ImageScreen(src = self.pageslist[self.pageindex])
        self.myScreenManager.switch_to(imgscreen)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None

    def on_keyboard_down(self,keyboard,keycode,text,modifiers):
        # keycode is a tuple of the form (int,str)
        # key pressed as str is therefore == keycode[1]
        if keycode[1]=='left' or keycode[1]=='a':
            self.prevPage()
            return True
        elif keycode[1]=='right' or keycode[1]=='d':
            self.nextPage()
            return True
        elif keycode[1] == 'backspace':
            Window.restore()
            self.myRootScreenManager.returnToHome()

    def prevPage(self):
        if self.pageindex == 0:
            # first page in chapter, jump to previous
            self.prevChapter(None)
        else:
            self.pageindex -= 1
            self.myScreenManager.transition.direction='right'
            self.PageSpinner.text = self.pagesFilenames[self.pageindex]

    def nextPage(self):
        if self.pageindex == (len(self.pageslist)-1):
            # last page in chapter, jump to next
            self.nextChapter(None)
        else:
            self.pageindex += 1
            self.myScreenManager.transition.direction = 'left'
            self.PageSpinner.text = self.pagesFilenames[self.pageindex]

    def prevChapter(self,button):
        if self.chapterindex == 0:
            # no chapter before this, give alert
            p = Popup(title="Alert",content=Label(text="You have reached the first page of the first chapter!"),size_hint=(0.4,0.4))
            p.open()
        else:
            # jump to previous chapter
            self.flag_FromSpinner = False
            self.chapterindex -= 1
            chapterpath = join(self.basepath,self.chapterslist[self.chapterindex])
            self.pageslist = map(lambda x: join(chapterpath,x), getPages(chapterpath))
            # last page of prev if using keys, first page if button
            if button != None:
                self.pageindex = 0
            else:
                self.pageindex = len(self.pageslist) - 1
            self.myScreenManager.transition.direction='right'
            self.ChapterSpinner.text = self.chapterslist[self.chapterindex]

    def nextChapter(self,button):
        if self.chapterindex == (len(self.chapterslist)-1):
            # no chapter after this, give alert
            p = Popup(title="Alert",content=Label(text="You have reached the last page of the last chapter!"),size_hint=(0.4,0.4))
            p.open()
        else:
            # jump to next chapter.
            # Doesn't matter by key or button, go to first page
            self.flag_FromSpinner = False
            self.myScreenManager.transition.direction = 'left'
            self.chapterindex += 1
            self.pageindex = 0
            self.ChapterSpinner.text = self.chapterslist[self.chapterindex]

class ImageScreen(Screen):
    '''
    Screen consisting of only one Image widget
    '''
    src = StringProperty() #This src corresponds to the image file
