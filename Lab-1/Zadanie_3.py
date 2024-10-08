RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'


if __name__ == '__main__':
    for i in range(9):
        print(9-i, f'{'  '*(9-i-1)}{RED}{"  "}{END}')

    print('  0  1 2 3 4 5 6 7 8 9')