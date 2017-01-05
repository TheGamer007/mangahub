from kivy.app import App
from homescreen import TextHomeScreen
from imageviewscreen import ImageViewScreen
from seriesscreen import SeriesScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from os import listdir
class RootScreenManager(ScreenManager):
    '''
    The topmost ScreenManager widget in the application, that also
    serves as the root widget
    '''
    pass

class MangaHubApp(App):
    '''
    Kivy App class
    '''
    def build(self):
        myScreenManager = RootScreenManager()
        myScreenManager.add_widget(TextHomeScreen())
        return myScreenManager

if __name__ == '__main__':
    MangaHubApp().run()
