def print_board():
"""
Prints current board
"""
    print('---------')
    for i in range(len(choices_list)):
        if i == 0 or i == 3 or i == 6:
            print('|' + ' ' + str(choices_list[i]) + ' ', end='')
        elif i == 2 or i == 5 or i == 8:
            print(str(choices_list[i]) + ' ' + '|')
        else:
            print(str(choices_list[i]) + ' ', end='')
    print('---------')

def checker():
"""
Checks if game over: if there is a winner or draw
"""
    global game_finished
    if choices_list.count('_') < 5:     # check if X or O won after 4 moves
        if abs(choices_list.count('X') - choices_list.count('O')) > 1:
            print('Impossible')
        elif choices_list[0] == choices_list[1] == choices_list[2] != '_':    # across top
            if choices_list[3] == choices_list[4] == choices_list[5] != '_':
                print("Impossible")
            elif choices_list[6] == choices_list[7] == choices_list[8] != '_':
                print("Impossible")
            else:
                game_finished = 1
                if choices_list[0] == 'X':
                    print('X wins')
                else:
                    print('O wins')
        elif choices_list[3] == choices_list[4] == choices_list[5] != '_':  # across middle
            if choices_list[0] == choices_list[1] == choices_list[2] != '_':
                print("Impossible")
            elif choices_list[6] == choices_list[7] == choices_list[8] != '_':
                print("Impossible")
            else:
                game_finished = 1
                if choices_list[3] == 'X':
                    print('X wins')
                else:
                    print('O wins')
        elif choices_list[6] == choices_list[7] == choices_list[8] != '_':  # across bottom
            if choices_list[0] == choices_list[1] == choices_list[2] != '_':
                print("Impossible")
            elif choices_list[3] == choices_list[4] == choices_list[5] != '_':
                print("Impossible")
            else:
                game_finished = 1
                if choices_list[6] == 'X':
                    print('X wins')
                else:
                    print('O wins')
        elif choices_list[0] == choices_list[3] == choices_list[6] != '_':  # down left
            if choices_list[1] == choices_list[4] == choices_list[7] != '_':
                print("Impossible")
            elif choices_list[2] == choices_list[5] == choices_list[8] != '_':
                print("Impossible")
            else:
                game_finished = 1
                if choices_list[0] == 'X':
                    print('X wins')
                else:
                    print('O wins')
        elif choices_list[1] == choices_list[4] == choices_list[7] != '_':  # down middle
            if choices_list[0] == choices_list[3] == choices_list[6] != '_':
                print("Impossible")
            elif choices_list[2] == choices_list[5] == choices_list[8] != '_':
                print("Impossible")
            else:
                game_finished = 1
                if choices_list[1] == 'X':
                    print('X wins')
                else:
                    print('O wins')
        elif choices_list[2] == choices_list[5] == choices_list[8] != '_':  # down right
            if choices_list[0] == choices_list[3] == choices_list[6] != '_':
                print("Impossible")
            elif choices_list[1] == choices_list[4] == choices_list[7] != '_':
                print("Impossible")
            else:
                game_finished = 1
                if choices_list[2] == 'X':
                    print('X wins')
                else:
                    print('O wins')
        elif choices_list[0] == choices_list[4] == choices_list[8] != '_':  # diagonal
            game_finished = 1
            if choices_list[0] == 'X':
                print('X wins')
            else:
                print('O wins')
        elif choices_list[2] == choices_list[4] == choices_list[6] != '_':  # diagonal
            game_finished = 1
            if choices_list[2] == 'X':
                print('X wins')
            else:
                print('O wins')
        else:
            if abs(choices_list.count('X') - choices_list.count('O')) > 1:
                print('Impossible')
            elif choices_list.count('_') == 0:
                game_finished = 1
                print('Draw')
    elif abs(choices_list.count('X') - choices_list.count('O')) > 1:
        print('Impossible')

def switcher():
"""
Switches players from X to O and vice-versa
"""
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

def game():
"""
Main game function that takes coordinates as moves
"""
    while True:
        try:
            x, y = input("Enter the coordinates: ").split()
        except:
            print("You should enter numbers!")
        else:
            break
        
    while True:
        if x == '1' and y == '1':
            if choices_list[6] == '_':
                choices_list[6] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '1' and y == '2':
            if choices_list[3] == '_':
                choices_list[3] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '1' and y == '3':
            if choices_list[0] == '_':
                choices_list[0] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '2' and y == '1':
            if choices_list[7] == '_':
                choices_list[7] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '2' and y == '2':
            if choices_list[4] == '_':
                choices_list[4] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '2' and y == '3':
            if choices_list[1] == '_':
                choices_list[1] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '3' and y == '1':
            if choices_list[8] == '_':
                choices_list[8] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '3' and y == '2':
            if choices_list[5] == '_':
                choices_list[5] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        elif x == '3' and y == '3':
            if choices_list[2] == '_':
                choices_list[2] = player
            else:
                print("This cell is occupied! Choose another one!")
                game()
            break
        else:
            print("Coordinates should be from 1 to 3!")
            game()
        break


# Main code
player = 'X'            # Starting player is X
game_finished = 0       # Set to 1 when game is finished
choices = '_________'   # Starting grid

# This let's you set up the starting board if you don't want to start from blank
# while True:
#     choices = input("Enter cells: ")
#     if len(choices) != 9:
#         print("Please enter exactly 9 characters")
#         continue
#     break

choices_list = []
choices_list = [x for x in choices]
#choices_list = list(choices)       # another way to do it

print_board()

while game_finished == 0:
    game()
    switcher()
    print_board()
    checker()
