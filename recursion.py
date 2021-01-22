
def factorial(n):
    """
        Calculates a number factorial
        :param n > 0
        :returns n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


def run():
    n = int(input('Type a number: '))
    print(f'The factorial of {n} is {factorial(n)}')


if __name__ == '__main__':
    run()
