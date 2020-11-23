from microbit import *
import radio
radio.config(group=73)
radio.on()


board = "00000:00000:00000:00000:00000"
while True:
    if pin0.read_digital():
        display.clear()
        newBoard = list(board)
        newBoard[1] = '1'
        newBoard[0] = '0'
        board = ''.join(newBoard)
        display.show(Image(
         board))
        radio.send('moving')
    if pin11.read_digital():
        display.clear()
        newBoard = list(board)
        newBoard[0] = '9'
        board = ''.join(newBoard)
        display.show(Image(
         board))
        radio.send('still')
    sleep(1000)



