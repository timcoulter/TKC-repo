from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from math import sqrt, ceil

def main():
    names = []
    user_input = input('autofill or enter names (y = autofill, n = enter manually)\n>>>')
    if user_input == 'y':
        name = input('Enter a name\n>>>').strip()
        cells = 0
        while cells <= 0:
            try:
                cells = int(input('How many times would you like to label your name?\n>>>'))
            except ValueError:
                print('must be integer and above 0!')
        for number in range(0, cells):
            names.append(name)
    elif user_input == 'n':
        name = str()
        while name != 'q':
            name = input('Enter a name (or "q" to quit)\n>>>')
            names.append(name)
    else:
        print('"y" or "n" must be entered!')
        main()

    box = 'BoxLayout:\n'
    tab = '\t'
    vertical = "orientation: 'vertical'\n"
    horizontal = "orientation: 'horizontal'\n"
    label = 'Label:\n'
    text = 'text: '
    SIZE = ceil(sqrt(len(names))) ** 2
    SQRT = int(sqrt(SIZE))
    output = str()

    with open('name_labels.kv', 'w') as file:
        for num in range(0, SQRT):
            output += num * tab + box + (num + 1) * tab
            if num == 0:
                output +=
            if num % 2 == 0:
                orientation = vertical
            else:
                orientation = horizontal
            output += orientation
        for i in range(0, SIZE):
            if i >= len(names):
                break
            elif i % SQRT == 0 and i != 0:
                output += (SQRT - 1) * tab + box + SQRT * tab + orientation + SQRT * tab + label + (
                                                                                                       SQRT + 1) * tab + text + "'" + \
                          names[i] + "'\n"
            else:
                output += SQRT * tab + label + (SQRT + 1) * tab + text + "'" + names[i] + "'\n"
        file.write(output)

    class NameLabels(App):
        """ NameLabels is a Kivy App that displays names from a list"""
        def build(self):
            """ build the Kivy app from the kv file """
            Window.size = (1200, 800)
            self.title = "Name Labels"
            self.root = Builder.load_file('name_labels.kv')
            return self.root
    NameLabels().run()

main()

