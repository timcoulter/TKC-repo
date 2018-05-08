"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())
    os.chdir('Lyrics')
    print(os.listdir('.'))

    for filename in os.listdir('.'):
        if filename == 'cleanup_files.py' or filename == 'temp':
           continue
        else:
            print('Files in the directory >>> {0}'.format(filename))
            for subfiles in os.listdir(filename):
                subfiles = get_fixed_filename(subfiles)
                print(subfiles)

def get_fixed_filename(filename):
    new_name = ""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, char in enumerate(filename, 0):
        if i == 0 or filename[i-1] == '_' or filename[i-1] == '(':
            new_name += char.upper()
        elif char.isupper() and filename[i-1] != '_' or char == '(':
            new_name += ('_' + char)
        else:
            new_name += char
    return new_name
main()


