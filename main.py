from kivy.app import App
from homescreen import TextHomeScreen
from imageviewscreen import ImageViewScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

class RootScreenManager(ScreenManager):
    '''
    The topmost ScreenManager widget in the application that also
    serves as the root widget.
    '''
    def returnToHome(self):
        self.switch_to(TextHomeScreen(self))

    def openImageScreen(self,basepath,chapters,chapterindex,pageindex):
        myImageViewScreen = ImageViewScreen(basepath=basepath,chapters=chapters,chapterindex=chapterindex,pageindex=pageindex)
        myImageViewScreen.myRootScreenManager = self
        self.switch_to(myImageViewScreen)
        Window.maximize()

class MangaHubApp(App):
    '''
    Kivy App class.
    '''
    def build(self):
        myScreenManager = RootScreenManager()
        myScreenManager.add_widget(TextHomeScreen(myScreenManager))
        return myScreenManager

if __name__ == '__main__':
    MangaHubApp().run()
