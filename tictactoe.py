# -*- coding: utf-8 -*-
"""
Tic tac toe
1-21-22
CJ's birthday :)
"""

# create sets for winning spot numbers
# rows, columns, diagonals
wins = [set([1,2,3]), set([4,5,6]), set([7,8,9]), set([1,4,7]), set([2,5,8]), set([3,6,9]), set([1,5,9]), set([3,5,7])]

import random

def start_board():
    """

    Returns
    -------
    4 strings.

    """
    l1 = '   |   |  '
    l2 = '   |   |  '
    l3 = '   |   |  '
    steady = '---+---+---'
    return(l1, l2, l3, steady)

# This will be used to make sure no space numbers are repeated
all_spaces = set(range(1,10))


def show_space_nums():
    """
    this shows the empty start board with numbering

    Returns
    -------
    None.

    """
    print("\n\n 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")
    print("\n\n")
    
    
def working_board(line1, line2, line3):
    """
    updates board when moves are made

    Parameters
    ----------
    line1 : TYPE
        DESCRIPTION.
    line2 : TYPE
        DESCRIPTION.
    line3 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print(line1)
    print(steady)
    print(line2)
    print(steady)
    print(line3)
    
    
def instructions():
    """
    shows instructions at beginning of game
    calls function to draw the start board

    Returns
    -------
    None.

    """
    print("\n\nInstructions")
    print("===============================================")
    print("This is what your board will look like.")
    print("Note the numbers in each space.  You will use those numbers to place your marker.")
    show_space_nums()
    
def winner_check(marks):
    """
    moves contains player's or computer's move numbers
    this will check to see if p_marks or c_marks has a winning set in it

    Parameters
    ----------
    moves : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    for win in wins:
        if win.issubset(set(marks)):
            return True
    return False
    
def place_player(turn, spot, mark, m, l1, l2, l3):
    
    """
    this takes in the info on whose turn it is, where the marker goes,
    what marker to use, and how many moves have been made
    it uses these to change the lines to get sent to the function
    that will print the new board
    """
    
    if turn == 'p':
        if(spot == 1):
            l1 = l1[0:1] + mark + l1[2:]
        elif(spot == 4):
            l2 = l2[0:1] + mark + l2[2:]
        elif(spot == 7):
            l3 = l3[0:1] + mark + l3[2:]
        elif(spot == 2):
            l1 = l1[0:5] + mark + l1[6:]
        elif(spot == 5):
            l2 = l2[0:5] + mark + l2[6:]
        elif(spot == 8):
            l3 = l3[0:5] + mark + l3[6:]
        elif(spot == 3):
            l1 = l1[0:9] + mark
        elif(spot == 6):
            l2 = l2[0:9] + mark
        else:
            l3 = l3[0:9] + mark
        # if m == 9:
        working_board(l1,l2,l3)
    
    if turn == 'c':
        if (m != 5):
            if(spot == 1):
                l1 = l1[0:1] + mark + l1[2:]
            elif(spot == 4):
                l2 = l2[0:1] + mark + l2[2:]
            elif(spot == 7):
                l3 = l3[0:1] + mark + l3[2:]
            elif(spot == 2):
                l1 = l1[0:5] + mark + l1[6:]
            elif(spot == 5):
                l2 = l2[0:5] + mark + l2[6:]
            elif(spot == 8):
                l3 = l3[0:5] + mark + l3[6:]
            elif(spot == 3):
                l1 = l1[0:9] + mark
            elif(spot == 6):
                l2 = l2[0:9] + mark
            else:
                l3 = l3[0:9] + mark
            working_board(l1, l2, l3)
    return l1, l2, l3
    
    
# One of these will be used after the player picks a spot on the board
replies = ['Nice! ',
           'Sweet. ',
           'Alrighty then. ',
           'Okay, okay. ',
           'Okie dokie']    



# Welcome to the game!
print("\n\n\nHi!  Let's play tic tac toe!")
play = True

# While player wants to play, keep playing the game
while(play):
    l1, l2, l3, steady = start_board()
    ans = input("Would you like to see the instructions? (y or n) ")
    if (ans == 'y'):
        instructions()
    
    # Assign x's or o's to human and machine
    p_mark = input("Would you like to be X or O? ")
    if(p_mark == 'o'):
        c_mark = 'x'
    elif(p_mark == 'O'):
        c_mark = 'X'
    elif(p_mark == 'x'):
        c_mark = 'o'
    else:
        c_mark = 'O'
        
    # Set up empty lists to keep track of occupied spots
    occ = []
    p_marks = []
    c_marks = []
    
    # set the initial spot to 0
    # p_spot = 0
    # Set moves to zero since not one went yet
    moves = 0
    # set winner equal to false
    p_wins = False
    c_wins = False
    winner = p_wins or c_wins
    # start the game; play as long as the board isn't full and no one has won
    while(len(occ) < 9 and not winner):
        # Get player spot
        p_spot = int(input("Enter the number where you want your " + p_mark + ": "))
        # Keep asking if the spot isn't valid
        while(p_spot in occ or p_spot not in range(1,10)):
            p_spot = int(input("Sorry, that spot is taken or is an invalid spot number. Try again: "))
        p_marks.append(p_spot)
        occ.append(p_spot)
        # count noves because on the 5th move, the computer doesn't get another turn
        moves += 1
        i = random.randint(0, len(replies)-1)
        print("\n\n" + replies[i])
        print("With your move:\n\n")
        l1, l2, l3 = place_player('p', p_spot, p_mark, moves, l1, l2, l3)
        p_wins = winner_check(p_marks)
        if p_wins:
            print("Congratulations!  You won!!!")
            break
            
        # generate computer spot
        occ_set = set(occ)
        available = all_spaces.difference(occ_set)
        if(moves < 9):
            c_spot = random.sample(available, 1)[0]
            occ.append(c_spot)
            c_marks.append(c_spot)
            # count noves because on the 5th move, the computer doesn't get another turn
            moves += 1
            print("\n\nWith my move:\n\n")
            l1, l2, l3 = place_player('c', c_spot, c_mark, moves, l1, l2, l3)
            c_wins = winner_check(c_marks)
            if c_wins:
                print("Awwwww.  You lost.")
                break
            
    
    
    ans = input("Would you like to play again? (y or n) ")
    if (ans == 'n' or ans == 'N'):
        play = False
        
    
# Let them know how many games they played, how many they won, and say thanks for playing!
print("\n\n*******************\nThanks for playing!\n*******************")