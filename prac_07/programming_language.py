import inspect

class ProgrammingLanguage:
    def __init__(self, name=None, typing=None, reflection=None, year=None):
        self.data = [name.title(), typing.strip().lower().title(), reflection, year]

    def __str__(self):
        return str('{0}, {1} Typing, Reflection={2}, First appeared in {3}'.format(self.data[0], self.data[1], self.data[2], self.data[3]))

    def is_dynamic(self):
        typing = self.data[1]
        if typing == 'Dynamic':
            return True
        else:
            return False
