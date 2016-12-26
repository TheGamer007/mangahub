from kivy.app import App
from homescreen import TextHomeScreen

class MangaHubApp(App):
    '''
    Kivy App class
    '''
    def build(self):
        return TextHomeScreen()

if __name__ == '__main__':
    MangaHubApp().run()
