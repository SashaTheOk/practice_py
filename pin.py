initial_pin = '1234'


n = 0
max_tries = 3

while n < 3:

    user_pin = input('Enter your pin: ')

    if len(user_pin) == 4 or len(user_pin) == 6:

        if initial_pin == user_pin:

            amount = input('How much: ')
            print(f'Take your {amount}')
            break

        else:

            print('Sorry, wrong pin. Try again pleas!')
            print(f'You have {max_tries-n-1} tries')
            n += 1

    else:
        print('Pin should be 4 or 6 digits!')

print('Good bye!')
