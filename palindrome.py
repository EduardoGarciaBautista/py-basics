def main():
    word = input('Write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome:
        print('Is palindrome')
    else:
        print('Is not palindrome')


def palindrome(word):
    word = word.strip().lower().replace(' ', '')
    newWord = word[::-1]
    return word == newWord


if __name__ == '__main__':
    main()
