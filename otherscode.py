from microbit import *
import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''

# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Table
tab=range(1,10)

def print_board():
    dup = board.copy()  
    for count, item in enumerate(dup):
        if item=='X':
            dup[count]='9'
        elif item=='O':
            dup[count]='5'
        else:
            dup[count]='0'

    dup.insert(0,'0')
    dup.insert(4,'0')
    dup.insert(5,'0')
    dup.insert(9,'0')
    dup.insert(10,'0')
    dup.insert(14,'0')
    dup.insert(15,'0')
    dup.insert(19,'0')
    dup.insert(20,'0')
    dup.insert(24,'0')
    dup.insert(5,':')
    dup.insert(11,':')
    dup.insert(17,':')
    dup.insert(0,'0')
    dup.insert(0,'0')
    dup.insert(0,'0')
    dup.insert(0,'0')
    dup.insert(0,'0')
    dup.insert(5,':')
    str = ''.join(dup)
    display.show(Image(str))
    
        
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x)
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

# AI goes here
def computer_move():
    move=-1
    # If I can win, others don't matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        # If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

def space_exist():
    return board.count('X') + board.count('O') != 9

player, computer = ('X','O')
result='%%% Deuce ! %%%'
# avoid the first round problem
sideEf = 0;
display.scroll("Welcome")
while space_exist():
    
    print_board()
    if sideEf==0:
      pin0.read_digital()
      pin1.read_digital()
      pin2.read_digital()
      #pin3.read_digital()
      #pin4.read_digital()
      #pin5.read_digital()
      #pin6.read_digital()
      #pin7.read_digital()
      pin8.read_digital()
      #pin9.read_digital()
      pin12.read_digital()
      pin13.read_digital()
      pin14.read_digital()
      pin15.read_digital()
      pin16.read_digital()
      sideEf = sideEf+1
      continue
      sleep(1000)
    else:
        sleep(1000)
     
    move = None
    while move==None:
        if pin0.read_digital():
            move = 1
        elif pin1.read_digital():
            move = 2
        elif pin2.read_digital():
            move = 3
        #elif pin3.read_digital():
         #   move = 4
        #elif pin4.read_digital():
         #   move = 5
        #elif pin5.read_digital():
        #    move = 6
        #elif pin6.read_digital():
        #    move = 7
        #elif pin7.read_digital():
        #    move = 8
        elif pin8.read_digital():
            move = 4
        elif pin12.read_digital():
            move = 5
        elif pin13.read_digital():
            move = 6
        elif pin14.read_digital():
            move = 7
        elif pin15.read_digital():
            move = 8
        elif pin16.read_digital():
            move = 9
        
    #board[0] = 'X'
    moved, won = make_move(board, player, move)
    sleep(1000)
    if won:
        display.scroll("Good Job")
        break
    elif computer_move()[1]:
        display.scroll("Try Again")
        break
    sideEf = sideEf+1


        

