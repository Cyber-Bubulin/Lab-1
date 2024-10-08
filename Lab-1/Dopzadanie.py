RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'

import time
SET_COLOR = "\x1b[48;5;"
END = '\x1b[0m'
CLEAR = "\033[H"


def draw_line(length = 5, color = 78, offset = 0):
    print(f"{' '*offset}{SET_COLOR}{i}m{' '*length}{END}")


if __name__ == '__main__':
    for i in range(1, 30):
        draw_line(i, i, i)
        print(f"{CLEAR}")
        time.sleep(0.5)

    
