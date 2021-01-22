def run():
    target = int(input('Type a number: '))
    epsilon = 0.01
    step = epsilon ** 2
    response = 0.0

    while abs(response ** 2 - target) >= epsilon and response <= target:
        print(abs(response ** 2 - target))
        response += step
    if abs(response ** 2 - target) >= epsilon:
        print(f'Square root not found')
    else:
        print(f'The square root of {target} is {response}')


if __name__ == '__main__':
    run()
