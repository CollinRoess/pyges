import os
import pandas as pd

def get_file(file_name):
    global file
    file = open(os.path.abspath(file_name))


if __name__ == '__main__':
    print('NOTE: Filenames must be in the same directory as this program')
    file_name =  input('Please enter a filename, or enter \'(h)elp\': ')
    if file_name == 'h' or file_name == 'H':
        get_file('readme.md')
        print(file.read())
    else:
        get_file(file_name)
