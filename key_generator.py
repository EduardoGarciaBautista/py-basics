import random


def generate_password():
    upper = ['A','B', 'C', 'D', 'E', 'F', 'G']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '%', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7']

    characters = upper + lower + symbols + numbers

    password = []

    for i in range(15):
        password.append(random.choice(characters))

    return ''.join(password)


def run():
    password = generate_password()
    print('Your password is: ' + password)


if __name__ == '__main__':
    run()
