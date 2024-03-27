### Create a dictionary with key = name and value = birthday from an input list
def create_dict(lst):

    # Create a empty dictionary
    birth_dict = {}

    # Loop on list
    for item in lst:

        # Alocate first part to key and second part for value
        birth_dict[item.split('-')[0]] = item.split('-')[1]
    
    return birth_dict