def run():
    # Is a data structure based on key > value

    my_dictionary = {
        'name': 'Eduardo',
        'last_name': 'Garcia Bautista'
    }
    print(my_dictionary['name'])
    print(my_dictionary['last_name'])
    print('##############<Keys>###################')

    for prop in my_dictionary.keys():
        print(prop)

    print('####################<Values>##################')
    for prop in my_dictionary.values():
        print(prop)

    print('####################<Both values>##################')
    for key, value in my_dictionary.items():
        print(key)
        print(value)




if __name__ == '__main__':
    run()
