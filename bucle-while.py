# counter = 0
#
# print('2 to ' + str(counter) + 'is = to: ' + str(2 ** counter))
#
#
# counter = 2
#
# print('2 to ' + str(counter) + 'is = to: ' + str(2 ** counter))
#

def run():
    LIMIT = 1000000

    counter = 0

    potency = 2 ** counter

    while potency < LIMIT:
        print('2 to ' + str(counter) + ' is = to: ' + str(potency))
        counter += 1
        potency = 2**counter


if __name__ == '__main__':
    run()
