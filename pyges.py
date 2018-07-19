import os
import pandas as pd

def get_file(file_name):
    global file
    file = open(os.path.abspath(file_name))

def print_text(file):
    for line in file:
        print(line)

def get_parametric_data(file):
    global x
    x=[]
    for line in file:
        if line[72]=='P':
            x.append(line[:65])
def get_points():
    y=[]
    pointlist=[]
    for item in x:
        item=item.split(';')
        y.append(item[0])
    for item in y:
        pointlist.append(item.strip('\'').split(','))

    '''[x.strip('\'') for x in pointlist]'''
    true_pointlist=[]
    for item in pointlist:
        for i in item:
            true_pointlist.append(i)
    print (set(true_pointlist))



if __name__ == '__main__':
    print('NOTE: Filenames must be in the same directory as this program')
    file_name =  input('Please enter a filename, or enter \'(h)elp\': ')
    if file_name == 'h' or file_name == 'H':
        get_file('readme.md')
        print(file.read())
    else:
        get_file(file_name)
        get_parametric_data(file)
        get_points()
