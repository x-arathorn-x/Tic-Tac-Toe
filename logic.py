# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    if (board[0][0] == board[0][1] == board[0][2]):
        return(board[0][0])
    elif (board[1][0] == board[1][1] == board[1][2]):
        return(board[1][0])
    elif (board[2][0] == board[2][1] == board[2][2]):
        return(board[2][0])
    elif (board[0][0] == board[1][0] == board[2][0]):
        return(board[0][0])
    elif (board[0][1] == board[1][1] == board[2][1]):
        return(board[0][1])
    elif (board[0][2] == board[1][2] == board[2][2]):
        return(board[0][2])
    elif (board[0][0] == board[1][1] == board[2][2]):
        return(board[0][0])
    elif (board[0][2] == board[1][1] == board[2][0]):
        return(board[0][2])
    else:
        return None
    


def other_player(player):
    """Given the character for a player, returns the other player."""

    if player == "X":

        return "O"  # FIXME
    else:
        return "X"
    
#    if player == max_player:  
#                # X is max player
#                if sim_score['score'] > best['score']:
#                    best = sim_score
#            else:
#                if sim_score['score'] < best['score']:
#                    best = sim_score
#        return best
