# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, other_player, get_winner


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = "X"
    while winner == None:
        
    
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print(board)

        # TODO: Input a move from the player.
        #also make sure the move is valid

        current_x_coor = int(input("Please input the x coordinate you wish to change "))
        current_y_coor = int(input("Please input the y coordinate you wish to change "))
        current_player = None

        # TODO: Update the board.
        
        board[current_y_coor][current_x_coor] = player
        player = other_player(player)
        
                    




        # TODO: Update who's turn it is.
        

        winner = get_winner(board)
        print(winner)
        #winner = 'X'  # FIXME