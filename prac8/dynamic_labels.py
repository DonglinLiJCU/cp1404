from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


NEW_COLOUR = (1, 0, 0, 1)

class DynamicLabels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            # create a button for each data entry, specifying the text
            tmp_label = Label(text=name)
            # set the button's background colour
            tmp_label.background_color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(tmp_label)

DynamicLabels().run()