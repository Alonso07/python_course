import os
import random


def player_input():
    marker = ''
    valid_ops = ('X' , 'O')
    
    while marker not in valid_ops:
        marker = input('Player 1, choose X or O: ')
        if marker not in valid_ops:
            print("Not a valid option, it must be {}".format(valid_ops))
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)
    
    
def display_board(board):
    os.system('cls')
    print(" | ".join(board[6:9]))
    print("--+---+---")
    print(" | ".join(board[3:6]))
    print("--+---+---")
    print(" | ".join(board[0:3]))
    

def place_marker(board, marker, position):
    board[position - 1] = marker
    return board


def win_check(board, mark):
    if len(set([board[0],board[1],board[2]])) == 1:
        return True
    if len(set([board[3],board[4],board[5]])) == 1:
         return True
    if len(set([board[6],board[7],board[8]])) == 1:
         return True
    if len(set([board[0],board[3],board[6]])) == 1:
         return True
    if len(set([board[1],board[4],board[7]])) == 1:
         return True
    if len(set([board[2],board[5],board[8]])) == 1:
         return True
    if len(set([board[0],board[4],board[8]])) == 1:
         return True
    if len(set([board[2],board[4],board[6]])) == 1:
         return True         
    else: 
        return False


def choose_first():
    return random.randint(1, 2)
    
  
def space_check(board, position):
    slot = board[position - 1]
    if  slot == 'X' or slot == 'O':
        return False
    return True
    

def full_board_check(board):
    ctr = 0
    int_board = board
    for ele in board:
        if ele in ['X', 'O']:
            ctr += 1
    #print(ctr)
    if ctr != 9:
        return False
    else:
        return True


def player_choice_pos(board):
    number = "Wrong "
    validated = False
    
    while not validated:
        number = input("Enter new available position (1-9): ")
        if number.isdigit() == True:
            numberDig = int(number)
            if 1 <= numberDig <= 9:
                if space_check(board, numberDig):
                    validated = True
                else:
                    print("Space not available!")
            else:
                print("Value out of range!")
        else:
            print("Input is not digit!")
    return numberDig
        
        
def replay_():
    option = "NV"
    valid_opt = ['Y', 'N']
    while option not in valid_opt:
        option = input("Do you want to replay? (Y/N): ")
        if option not in valid_opt:
            print("Input not valid try Y or N")
    if option == 'Y':
        return True
    else:
        return False
            
    


print("Welcome to Tic Tac Toe!")

replay = True


while replay:
    ## set the game up here
    game_on = True
    board = ['1','2','3','4','5','6','7','8','9']
    player = choose_first()
    players = player_input()
    
    while game_on:
        # Player 1 Turn
        display_board(board)
        position = player_choice_pos(board)
        board = place_marker(board, players[0], position)
        if win_check(board, players[0]):
            print("Player 1 {} won ".format(players[0]))
            game_on = False
            break
        
        # Player 2 turn.
        display_board(board)
        position = player_choice_pos(board)
        board = place_marker(board, players[1], position)
        if win_check(board, players[1]):
            print("Player 2 {} won ".format(players[1]))
            game_on = False
            break
        
        if full_board_check(board):
            print("Game went to tie:")
            game_on = False
        
        
    replay = replay_()


