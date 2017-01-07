from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty,ListProperty
from library import getAllSeries,SourcesDialogContent,getChapters
from seriesscreen import SeriesScreen
from os.path import join
from kivy.uix.screenmanager import Screen

class BookCover(Label):
    '''
    An extension of Label that is suited for displaying book cover thumbnails.
    Primary element of the main HomeScreen
    '''
    pass

class HomeScreen(GridLayout):
    '''
    The main class which will be used to display the HomeScreen in the
    final application
    '''
    pass

class TextHomeScreen(Screen):
    '''
    A HomeScreen with minimal text-based design for testing purposes
    '''
    titles = ListProperty() # list of (source_path,series_name) tuples
    myRootScreenManager = None

    def __init__(self,screenmanager,**kwargs):
        super(TextHomeScreen,self).__init__(**kwargs)
        self.myRootScreenManager = screenmanager
        self.titles = getAllSeries()

    def openSourcesDialog(self,button):
        modal = ModalView(size_hint=(0.7,0.7))
        s = SourcesDialogContent()
        s.ids['btn_cls'].bind(on_release=modal.dismiss)
        modal.add_widget(s)
        modal.bind(on_dismiss=self.onPopupClosed)
        modal.open()

    def onPopupClosed(self,instance):
        #refresh the series listing
        self.titles = getAllSeries()

    def on_titles(self,instance,value):
        catalog = self.ids.layout_catalog
        #remove old labels
        catalog.clear_widgets()
        #add new labels
        for series_tuple in value:
            item = TextItem()
            # os.path.join takes care of trailing slashes and uses proper
            # seperators. Both the passed arguments should also be valid
            # since they were obtained through filechooser and os.listdir
            item.path = join(series_tuple[0],series_tuple[1])
            item.text = series_tuple[1]
            item.myRootScreenManager = self.myRootScreenManager
            catalog.add_widget(item)

class TextItem(BoxLayout):
    '''
    The primary element in the TextHomeScreen. A single row consisting
    of the title
    '''
    text = StringProperty()
    path = StringProperty() # This is path to the series, not a chapter
    myRootScreenManager = None

    def buttonClicked(self,button):
        mySeriesScreen = SeriesScreen()
        # Passing chapters while initiating: SeriesScreen(chapters=[blah,blah])
        # gives Attribute Error due to self.ids.chapter_list not being found
        # Likey cause is __init__ not being called before on_chapters. Hence, assign chapters seperately as below.
        # For the same reason, it is very important that the path StringProperty be assigned
        # before chapters ListProperty. Otherwise, basepath will be taken as default '' when on_chapters is run
        mySeriesScreen.basepath = self.path
        mySeriesScreen.myRootScreenManager = self.myRootScreenManager
        mySeriesScreen.chapters = getChapters(self.path)
        mySeriesScreen.ids.chapter_name.text = self.text
        self.myRootScreenManager.switch_to(mySeriesScreen)
