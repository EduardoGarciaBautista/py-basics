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

    a = [1, 2, 3, 4]
    b = a  # This make that both variables where pointing to the same direction
    print(id(a))
    print(id(b))
    final = [a, b]
    print(final)
    a.append(5)  # Side effect
    print(final)

    # Cloning list
    a = [1, 2, 3]
    b = a
    print(id(a))
    print(id(b))
    c = list(a)  # Is another list(clone)
    print(id(c))

    d = a[::]  # Another way to clone
    print(d)
    print(id(d))

    # List comprehensions

    my_list = list(range(0, 100))
    print(my_list)
    double = [i * 2 for i in my_list]

    print(double)

    par = [i for i in my_list if i % 2 == 0]
    print(par)


if __name__ == '__main__':
    run()
