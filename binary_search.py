# Binary search only works when the elements are in order
"""
    Calculates square root of a number but not exactly,is a proxime value
    :parameter not have parameters
    :returns have not returns parameters
"""


# To read this whit command help(run)

def run():
    target = int(input('Type a number: '))

    epsilon = 0.01

    down = 0.0
    high = max(1.0, target)

    response = high + down / 2

    while abs(response ** 2 - target) >= epsilon:
        if response ** 2 < target:
            down = response
        else:
            high = response
        response = (high + down) / 2

    print(f'The square root of {target} is {response}')


if __name__ == '__main__':
    run()
