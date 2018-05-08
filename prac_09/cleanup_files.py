"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os
import heapq


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    os.chdir('Lyrics')
    print(os.listdir('.'))
    #os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        print('Files in the directory >>> {0}'.format(filename))
        for subfiles in os.listdir(filename):
            print(subfiles)
            subfiles = get_fixed_filename(subfiles)
            print(subfiles)
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

def get_fixed_filename(filename):
    new_name = ""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, char in enumerate(filename, 0):
        last_char = i-1
        if i == 0 or filename[last_char] == '_' or filename[last_char] == '(':
            new_name += char.upper()
        elif char.isupper() and filename[last_char] != '_':
            new_name += ('_' + char)
        else:
            new_name += char
    return new_name

main()
