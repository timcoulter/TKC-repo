import inspect

class ProgrammingLanguage:
    def __init__(self, name=None, typing=None, reflection=None, year=None):
        self.name = name.title()
        self.typing = typing.strip().lower()
        self.reflection = reflection.lower().title().strip()
        self.year = year

    def __str__(self):
        return str('{}, {} Typing, Reflection={}, First appeared in {}'.format(self.name), self.typing, self.reflection, self.year )

    def is_dynamic(self):
        typing = self.typing
        if typing == 'dyanmic':
            print('{} is Dynamic!'.format(self.name))
        else:
            print('{} is not dynamic :('.format(self.name))



