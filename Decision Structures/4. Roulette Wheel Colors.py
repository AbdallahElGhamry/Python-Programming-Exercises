'''
On a roulette wheel, the pockets are numbered from 0 to 36. The
colors of the pockets are as follows:
	Pocket 0 is green.
	For pockets 1 through 10, the odd-numbered pockets are red
	and the even-numbered pockets are black.
	For pockets 11 through 18, the odd-numbered pockets are
	black and the even-numbered pockets are red.
	For pockets 19 through 28, the odd-numbered pockets are red
	and the even-numbered pockets are black.
	For pockets 29 through 36, the odd-numbered pockets are
	black and the even-numbered pockets are red.
Write a program that asks the user to enter a pocket number and
displays whether the pocket is green, red, or black. The program
should display an error message if the user enters a number that
is outside the range of 0 through 36.
'''


num = int(input('Enter an integer in range of 0 through 36: '))

if num == 0:
    print('Pocket', num, 'is green')
elif num >= 1 and num <= 10:
    if num % 2 == 0:
        print('Pocket', num, 'is black')
    else:
        print('Pocket', num, 'is red')
elif num >= 11 and num <= 18:
    if num % 2 == 0:
        print('Pocket', num, 'is red')
    else:
        print('Pocket', num, 'is black')
elif num >= 19 and num <= 28:
    if num % 2 == 0:
        print('Pocket', num, 'is black')
    else:
        print('Pocket', num, 'is red')
elif num >= 29 and num <= 36:
    if num % 2 == 0:
        print('Pocket', num, 'is red')
    else:
        print('Pocket', num, 'is black')
else:
    print('Invalid input.')


