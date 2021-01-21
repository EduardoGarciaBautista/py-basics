def is_prime(number):
    counter = 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1

    return counter == 0


def run():
    number = int(input('Type a number: '))
    if is_prime(number):
        print('Is prime')
    else:
        print('Is not Prime')


if __name__ == '__main__':
    run()
