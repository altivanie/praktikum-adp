from termcolor import cprint

atap= 11
for i in range(atap):
    print(' ' * (atap - i - 1), end='')
    cprint(' ' * (2 * i + 1), 'white', 'on_grey')

for i in range(2):
    print(' ', end='')
    cprint(' ' * 20, 'white', 'on_white')

for i in range(1, 7):
    if i == 2:
        print(' ', end='')
        cprint(' ' * 7, 'white', 'on_white', end='')
        cprint(' ', 'white', 'on_red', end='')
        cprint(' ' * 2, 'black', 'on_black', end='')
        cprint(' ' * 3, 'black', 'on_black', end='')
        cprint(' ' * 7, 'white', 'on_white')
    else:
        print(' ', end='')
        cprint(' ' * 7, 'white', 'on_white', end='')
        cprint(' ' * 4, 'black', 'on_black', end='')
        cprint(' ' * 9, 'white', 'on_white')