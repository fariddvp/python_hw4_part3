import os
from src.read_file import read_file
from src.create_dict import create_dict

def main():

    PATH = '/home/farid/Documents/hw4/python_hw4_part3/src/birthdays.txt'
    if not os.path.exists(PATH):
        print('There is not any file but we create a new file.')
        with open(PATH, 'w+') as f:
            pass

    birth_list = read_file(PATH) 
    print(birth_list) 

    birth_dict =  create_dict(birth_list)
    print(birth_dict)

    







main()