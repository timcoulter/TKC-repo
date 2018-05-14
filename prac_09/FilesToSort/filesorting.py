import os
import shutil
def sort_folders():
    extensions = list()
    categories = ['Docs', 'Images', 'Spreadsheets']
    for category in categories:
        if os.path.exists(os.getcwd() + '/' + category):
            shutil.rmtree(os.getcwd() + '/' + category)
        os.makedirs(os.getcwd() + '/' + category)
    for subfile in os.listdir(os.getcwd()):
        if subfile == 'filesorting.py' or os.path.isdir(os.getcwd() + '/' + subfile):
            continue
        elif os.path.exists(os.getcwd() + '/' + subfile.split('.')[1]):
            continue
        elif subfile.split('.')[1] not in extensions:
            extensions.append(subfile.split('.')[1])
            os.mkdir(subfile.split('.')[1])
        shutil.copy(subfile, subfile.split('.')[1])
        user_input = ''
        while user_input not in categories:
            user_input = input('What catergory would you like to sort {0} files into? '
                               .format(subfile.split('.')[1])).strip().lower()
            user_input = user_input.title()
            if user_input not in categories:
                print('{0} must be sorted into one of the following:\n\tDocs, Images, Spreadsheets'.
                      format(subfile.split('.')[1]))
        shutil.copy(subfile, user_input)

sort_folders()
