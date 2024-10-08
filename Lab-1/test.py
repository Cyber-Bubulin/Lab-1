RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'
                            

for  i in range(6):
   if i<3:
       print(f'{GREEN}{"  "*4}{YELLOW}{"  "*6}{END}')
   if i>=3:
       print(f'{GREEN}{"  "*4}{RED}{"  "*6}{END}')


# def draw_dual_romb(side = 8):
      
        for i in range(side):
            if i < side//2:
                print(f'{"  "*(side-i)}{BLACK}{"  "*(i*2)}{END}{"  "*((side//2-i)-1)}{"  "*(side//2-i)}{BLACK}{"  "*(i*2)}{END}')
            if i >= side//2:
                print(f'{"  "*(i)}{BLACK}{"  "*((side-i)*2)}{END}{"  "*((i-side//2)-1)}{"  "*(i-side//2)}{BLACK}{"  "*((side-i)*2)}{END}')
                
                
draw_dual_romb(16)

for i in range(9):
    print(9-i, f'{'  '*(9-i-1)}{RED}{"  "}{END}')

print('  0  1 2 3 4 5 6 7 8 9')



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
    
    
