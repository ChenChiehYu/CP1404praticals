from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (1, 0, 0, 1)


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = {"James": "Chen", "Bryan": "White", "Bronny": "Creak"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.label:
            temp_label = Label(text=name + " " + self.label[name])
            temp_label.background_color = NEW_COLOUR
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
