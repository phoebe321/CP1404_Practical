from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    def __init__(self, names=""):
        """Construct main app."""
        super().__init__()
        # basic data (model) example - dictionary of names: phone numbers
        self.names = names or ["Bob Brown", "Cat Cyan", "Oren Ochre", "Novia", "Elaine"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def add_label(self):
        main_layout = self.root.ids.main
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)

    def clear_labels(self):
        main_layout = self.root.ids.main
        main_layout.clear_widgets()


DynamicLabels().run()