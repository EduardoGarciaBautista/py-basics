def run():
    def divide(list_param, div):
        try:
            return [i / div for i in list_param]
        except ZeroDivisionError as e:
            print(e)
            return lists

    lists = list(range(10))
    divisor = 0
    print(divide(lists, divisor))


if __name__ == '__main__':
    run()
