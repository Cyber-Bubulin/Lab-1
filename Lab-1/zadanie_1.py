RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'
                            
if __name__ == '__main__':
    for  i in range(6):
        if i<3:
            print(f'{GREEN}{"  "*4}{YELLOW}{"  "*6}{END}')
        if i>=3:
            print(f'{GREEN}{"  "*4}{RED}{"  "*6}{END}')