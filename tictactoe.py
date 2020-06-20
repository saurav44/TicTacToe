board = {1:'-', 2:'-', 3:'-',
         4:'-', 5:'-', 6:'-',
         7:'-', 8:'-', 9:'-'}

def printBoard():
    print('\n')
    print( board[1] + ' | ' + board[2] + ' | ' + board[3] + '\t\t1|2|3')
    print( board[4] + ' | ' + board[5] + ' | ' + board[6] + '\t\t4|5|6')
    print( board[7] + ' | ' + board[8] + ' | ' + board[9] + '\t\t7|8|9')
    print('\n')
    
winner = False
player = 'X'
check = []

def check_rows():
    row1 = board[1] == board[2] == board[3] != '-'
    row2 = board[4] == board[5] == board[6] != '-'
    row3 = board[7] == board[8] == board[9] != '-'
    if (row1 or row2 or row3):
        return True

def check_columns():
    column1 = board[1] == board[4] == board[7] != '-'
    column2 = board[2] == board[5] == board[8] != '-'
    column3 = board[3] == board[6] == board[9] != '-'
    if (column1 or column2 or column3):
        return True
def check_diagnols():
    d1 = board[1] == board[5] == board[9] != '-'
    d2 = board[3] == board[5] == board[7] != '-'
    if d1 or d2:
        return True


def switch():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
        
while not winner:
    printBoard()
    print(player + "'s turn.")
    try:
        choice = int(input('Enter position from 1-9: '))
        if (choice in check) or (choice<1 or choice>9):
            print('*** Invalid position.\n      Enter correct position ***')
            continue
    except:
        print('*** Invalid position.\n      Enter correct position ***')
        continue
    check.append(choice)
    
    board[choice] = player

    if len(check) == 9:
        break
    
    winner = ( check_rows() or check_columns() or check_diagnols() )
    if winner == True:
        break
    switch()

printBoard()

if winner:
    print('Winner winner chicken dinner')
    print('And the winner is\n ' )
    print(' - - - ' + player + ' - - - ')
else:
    print(" Good Luck. It's a \n")
    print(' *** Tie *** ')
