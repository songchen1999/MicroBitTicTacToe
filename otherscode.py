from microbit import *
import radio
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
        if item=='O':
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
    str = ''.join(dup);
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

player, computer = select_char()
result='%%% Deuce ! %%%'
while space_exist():
    print_board()
    move = 1 if pin0.read_digital() else 0
    moved, won = make_move(board, player, move)
    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break

print_board()
