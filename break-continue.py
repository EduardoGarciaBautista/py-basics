def run():
    # Continue
    # for i in range(1000):
    #     if i % 2 != 0:
    #         continue
    #     print(i)

    # for i in range(10000):
    #     print(i)
    #     if i == 300:
    #         break

    text = input('Write a text: ')

    for char in text:
        if char == 'o':
            break
        print(char)


if __name__ == '__main__':
    run()
