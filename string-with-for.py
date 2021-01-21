def run ():
    # string = 'Hola Mundo'
    # for letter in string:
    #     print(letter)
    quote = input('Write some quote: ')

    for char in quote:
        print(char.upper())


if __name__ == '__main__':
    run()