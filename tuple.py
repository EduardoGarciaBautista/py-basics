def run():
    # number_list = [1, 2, 3, 4]
    # print(number_list)
    #
    # number_list2 = [5, 6, 7]
    # final_list = number_list + number_list2
    #
    # print(final_list)
    # Tuples are immutable
    # my_tuple = (1,) if only one element my_tuple take its type
    my_tuple = (1, 2, 3, 4, 'Hello')
    # print(my_tuple[0])
    # for el in my_tuple:
    #     print(el)

    x, y, z, a, b = my_tuple
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)

    def coordinates():
        return 5, 4

    x, y = coordinates()

    print(x)
    print(y)


if __name__ == '__main__':
    run()
