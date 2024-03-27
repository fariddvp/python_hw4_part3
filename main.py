import os
from src.read_file import read_file
from src.create_dict import create_dict
from src.add_to_file import add_to_file

def main():

    PATH = '/home/farid/Documents/hw4/python_hw4_part3/src/birthdays.txt'
    if not os.path.exists(PATH):
        print('There is not any file but we create a new file.')
        with open(PATH, 'w+') as f:
            pass
    
    birth_list = []
    birth_list = read_file(PATH) 
 
    birth_dict = {}
    birth_dict =  create_dict(birth_list)

    option = ''
    while option != '3':         
        print('_-_-_-_-_- menu _-_-_-_-_-')
        option = input('choose an option:\n\n\n'
                       '1- Search a name\n2- Add a new data\n3- Exit\n'
                       'enter 1 or 2 or 3 : ')
        
        # Search in birthday dict with name(key)
        if option == '1':
            name = input('Enter a name: ')
            if name in birth_dict:
                print(name + ' => ' + birth_dict[name])
            
            else:
                print(f'The is not {name} in dictionary')

        elif option == '2':
            name = input('Enter a name: ')
            birth_day, birth_month, birth_year = map(str,input('Enter birthday based on this type for example(12/February/1970) : ').split('/'))
            name_birthday = name + '-' + birth_day + ' ' + birth_month + ' ' + birth_year
            add_to_file(name_birthday)

        elif option == '3':
            exit()



main()