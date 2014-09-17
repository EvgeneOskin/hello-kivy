from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class HelloPhraseRenderer(BoxLayout):
    phrase_input = ObjectProperty()
    phrase_output = ObjectProperty()

    def render_phrase(self):
        if self.phrase_input.text:
            self.phrase_output.text, self.phrase_input.text = (
                self.phrase_input.text, ''
            )


class HelloApp(App):
    pass


if __name__ == '__main__':
    HelloApp().run()