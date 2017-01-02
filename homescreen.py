from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty,ListProperty
from library import getAllSeries,SourcesDialogContent
from time import sleep

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

    def getAllSeries(self):
        return getAllSeries()
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
        for title in value:
            item = TextItem()
            item.text = title
            catalog.add_widget(item)

class TextItem(BoxLayout):
    '''
    The primary element in the TextHomeScreen. A single row consisting
    of the title
    '''
    text = StringProperty()
