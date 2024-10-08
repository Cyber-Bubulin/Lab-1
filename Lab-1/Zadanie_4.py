RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'

if __name__=='__main__':
    sequence = open('sequence.txt')
    file = []
    for i in sequence:
        file.append(float(i))


    zerofive = []
    fivezero = []

    for i in file:
        if i> 0 and i <=5:
            zerofive.append(i)
        if i<0 and i>-5:
            fivezero.append(i)


    print('от 0 до 5  ' f'{BLUE}{' '*int((len(zerofive)/ len(file))*100)}{END}', (len(zerofive)/ len(file))*100,'%')
    print('от -5 до 0 ' f'{RED}{' '*int((len(fivezero)/ len(file))*100)}{END}', (len(fivezero)/ len(file))*100,'%')
    
    
