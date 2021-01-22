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
    # Get
    print('##########<Get>####################')
    print(my_dictionary.get('name'))
    print(my_dictionary.get('hola', 50))  # If a key does not exists returns 50

    my_dictionary['name'] = 'Juan'

    print(my_dictionary)

    del my_dictionary['name']  # Delete
    print(my_dictionary)

    # If a key exists inside
    print('name' in my_dictionary)


if __name__ == '__main__':
    run()
