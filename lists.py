# In python are named as lists

def run():
    numbers = [1, 2, 3, 4]
    print(numbers)
    numbers.append('Hello')
    print(numbers)

    numbers.pop(len(numbers) - 1)

    for el in numbers:
        print(el)

    print(numbers[::-1])


if __name__ == '__main__':
    run()
