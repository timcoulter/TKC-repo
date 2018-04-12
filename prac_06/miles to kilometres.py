from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesToKilometres(App):
    """ MilesToKilometres is a Kivy App for converting from miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('conversion.kv')
        self.miles = 10
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = self.miles * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """ handle calculation (could be button press or other call), output result to label widget """
        self.miles += increment
        self.root.ids.input_number.text = str(self.miles)


MilesToKilometres().run()