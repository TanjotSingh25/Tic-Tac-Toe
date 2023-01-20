"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                counter += 1
            elif board[i][j] == 'O':
                counter -= 1
    if counter == 0:
        return 'X'
    elif counter == 1:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action not in actions(board):
        raise NameError('Illegal Move')
    current_player = player(board)
    new_board[action[0]][action[1]] = current_player
    return new_board

def check_horizontal(board):
    for i in range(3):
        row = 0
        for j in range(3):
            if board[i][j] == 'X':
                row += 1
            elif board[i][j] == 'O':
                row -= 1
        if row == 3:
            return 'X'
        elif row == -3:
            return 'O'
    return None

def check_vertical(board):
    for i in range(3):
        column = 0
        for j in range(3):
            if board[j][i] == 'X':
                column += 1
            elif board[j][i] == 'O':
                column -= 1
        if column == 3:
            return 'X'
        elif column == -3:
            return 'O'
    return None

def check_diagonal(board):
    diag1 = 0
    diag2 = 0
    for i in range(3):
        if board[i][i] =='X':
            diag1 += 1
        elif board[i][i] == 'O':
            diag1 -= 1
        if board[2 - i][i] =='X':
            diag2 += 1
        elif board[2 - i][i] == 'O':
            diag2 -= 1
    if diag1 == 3 or diag2 == 3:
        return 'X'
    elif diag2 == -3 or diag2 == -3:
        return 'O'
    else:
        return None
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    horizontal = check_horizontal(board)
    vertical = check_vertical(board)
    diag = check_diagonal(board)
    if horizontal != None:
        return horizontal
    elif vertical != None:
        return vertical
    elif diag != None:
        return diag
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    final_winner = winner(board)
    if final_winner == 'X':
        return 1
    elif final_winner == 'O':
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        return minimax_recursive(board)[0]


def minimax_recursive(board):
    if terminal(board):
        return [(), utility(board)]

    current_player = player(board)
    if current_player == 'X':
        max_val = float('-inf')
        possible_actions = actions(board)
        best_move = possible_actions[0]
        for i in range(len(possible_actions)):
            temp = max_val
            max_val = max(max_val, minimax_recursive(result(board, possible_actions[i]))[1])
            if temp != max_val:
                best_move = possible_actions[i]
        return [best_move, max_val]
    elif current_player == 'O':
        min_val = float('inf')
        possible_actions = actions(board)
        best_move = possible_actions[0]
        for i in range(len(possible_actions)):
            temp = min_val
            min_val = min(min_val, minimax_recursive(result(board, possible_actions[i]))[1])
            if temp != min_val:
                best_move = possible_actions[i]
        return [best_move, min_val]