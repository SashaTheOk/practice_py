initial_pin = '1234'


n = 0

while n < 3:

    user_pin = input('Enter your pin: ')

    if len(user_pin) == 4 or len(user_pin) == 6:

        if initial_pin == user_pin:
            print('Here\'s you money')
            break
        else:
            print('Sorry, wrong pin. Try again pleas!')

    else:
        print('Pin should be 4 or 6 digits!')

    n += 1

print('gg')
