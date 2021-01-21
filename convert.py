def convert(peso_type, dollar_value):
    message = 'How ' + peso_type + ' pesos do you have?:  '
    pesos = float(input(message))

    dollars = pesos / dollar_value

    dollars = round(dollars, 2)

    dollars = str(dollars)

    print(f'You have ${dollars} dollars')


menu = """
Welcome to money convert ✌

1.- Colombian 
2.- Argentinian
3.- Mexican
Choose an option: 
"""

option = int(input(menu))

# money values
mexican = 19.56
colombian = 3875
argentinian = 65


if option == 1:
    convert('Colombian', colombian)
elif option == 2:
    convert('Argentinian', argentinian)
elif option == 3:
    convert('Mexican', mexican)
else:
    print('Chose a valid option')
