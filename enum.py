def run():
    target = int(input('Type a integer number: '))
    response = 0
    while response ** 2 < target:
        response += 1

    if response ** 2 == target:
        print(f'The square root of {response}')
    else:
        print(f'{target} hav not exact square root')


if __name__ == '__main__':
    run()
