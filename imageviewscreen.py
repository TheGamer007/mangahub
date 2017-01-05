from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.label import Label

class ImageViewScreen(Screen):
    '''
    Topmost widget that encompasses all buttons and
    an image screenmanager for displaying images
    '''
    myScreenManager = None
    pageslist = [] #this is expected to be a natural sorted list of paths to the images
    current_index = 0
    def __init__(self,pages,**kwargs):
        super(ImageViewScreen,self).__init__(**kwargs)
        self.myScreenManager = self.ids.images_manager
        self.pageslist = pages
        self.current_index = 0
        self.myScreenManager.switch_to(ImageScreen(src = self.pageslist[0]))
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
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index += 1 #negating the effect of decrement
            p = Popup(title="Alert",content=Label(text="You have reached the first page!"),size_hint=(0.4,0.4))
            p.open()
            return
        imgscreen = ImageScreen(src = self.pageslist[self.current_index])
        self.myScreenManager.switch_to(imgscreen,direction='right')
    def nextPage(self):
        #add check for last item in list
        self.current_index += 1
        if self.current_index >= len(self.pageslist):
            self.current_index -= 1 #negating the effect of increment
            p = Popup(title="Alert",content=Label(text="You have reached the last page!"),size_hint=(0.4,0.4))
            p.open()
            return
        imgscreen = ImageScreen(src = self.pageslist[self.current_index])
        self.myScreenManager.switch_to(imgscreen,direction='left')
class ImageScreen(Screen):
    '''
    Screen consisting of only one Image widget
    '''
    src = StringProperty() #This src corresponds to the image file
