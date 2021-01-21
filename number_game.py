import random


def run():
    random_number = random.randint(1, 100)
    message = 'Type a number between 1 and 100: '
    user_number = int(input(message))

    while user_number != random_number:
        if user_number < random_number:
            message = 'Type a high number: '
        else:
            message = 'Type a low number: '
        user_number = int(input(message))
    print('!You win¡')


if __name__ == '__main__':
    run()
