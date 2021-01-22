def run():
    my_range = range(0, 7, 2)
    print(my_range)

    other_range = range(0, 8, 2)
    print(other_range)

    print(id(my_range))
    print(id(other_range))

    print(my_range == other_range)  # Validate  (value equality)
    print(my_range is other_range)  # Validate  (object equality)

    # Par
    for i in range(0, 101, 2):
        print(i)

    # None

    for i in range(1, 99):
        if i % 2 != 0:
            print(f'{i} is none')


if __name__ == '__main__':
    run()
