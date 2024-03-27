import os

def read_file(path_file):

    if not os.path.exists(path_file):
        print('Error! there is not any file in your PATH.')

    birth_list = []
    with open(path_file, 'r') as r:
        for line in r:
            birth_list.append(line.strip())

    return birth_list