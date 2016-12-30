from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,ListProperty
from library import getSeries

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

class TextHomeScreen(BoxLayout):
    '''
    A HomeScreen with minimal text-based design for testing purposes
    '''
    titles = ListProperty()

    def getSeries(self,sourcepath):
        return getSeries(sourcepath)
    def __init__(self,**kwargs):
        super(TextHomeScreen,self).__init__(**kwargs)
        catalog = self.ids.layout_catalog
        for title in self.titles:
            item = TextItem()
            item.text = title
            catalog.add_widget(item)
        # Add a widget to take up the remaining space invisibly
        # This pushes the actual items up
        #catalog.add_widget(Widget())
        

class TextItem(BoxLayout):
    '''
    The primary element in the TextHomeScreen. A single row consisting
    of the title
    '''
    text = StringProperty()
    pass
