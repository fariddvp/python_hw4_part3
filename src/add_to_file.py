def add_to_file(data_string):
    PATH = '/home/farid/Documents/hw4/python_hw4_part3/src/birthdays.txt'
    try:
        with open(PATH, 'a') as f:
            f.write(data_string + '\n')
        print('Your data added.')
    except Exception as e:
        print('An error occurred while adding data to the file:', e)