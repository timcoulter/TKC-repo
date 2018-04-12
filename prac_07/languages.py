from programming_language import ProgrammingLanguage
languages = [ProgrammingLanguage('Ruby', 'Dynamic', True, 1995), ProgrammingLanguage('Python', 'Dynamic', True, 1991),
             ProgrammingLanguage('Visual Basic', 'Static', False, 1991)]
for language in languages:
    print(language)

print('The dynamically typed languages are: ')
for language in languages:
    if language.is_dynamic():
        print(language.data[0])



