from new import draw_board
from new import check_turn
from new import check_win
import os
spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",8:"8", 9:"9"}
playing = True
complete = False
turn = 0
prev_turn = -1
while playing:
    #reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print("Invaid spot selected, pick another spot")
    prev_turn = turn
    print("player ", str((turn % 2) +1),"'s trun: pick your spot or press q to quit")
    # get the input from the player
    choice = input()
    if choice =='q':
        playing = False
        #check if the player gives a num 1-9
    elif str.isdigit(choice) and  int(choice) in spots:
        #check if thespot has already been taken
        if not spots[int(choice)] in ["X", "O"]:
            #Valid input, update board
            turn += 1
            spots[int(choice)] = check_turn(turn)
#check if someone has won
    if check_win(spots): 
        playing = False
        complete = True
    if turn > 0:
        playing = False   
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#if draw
if complete:
    if check_turn(turn) == 'X': print("Player 1 Wins!")
    else:print("player 2 Wins!")
else:
    print("It a Draw")