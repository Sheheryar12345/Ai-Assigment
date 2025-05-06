import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
    print()

def check_winner(board):
    for player in [HUMAN, AI]:
        for i in range(3):
            if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
                return player
        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
            return player

    if all(cell != EMPTY for row in board for cell in row):
        return 'Draw'

    return None  # No winner yet

def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

def minimax(board, is_ai_turn):
    winner = check_winner(board)
    if winner == AI:
        return 1, None
    elif winner == HUMAN:
        return -1, None
    elif winner == 'Draw':
        return 0, None

    best_move = None
    if is_ai_turn:
        best_eval = -math.inf
        for row, col in get_available_moves(board):
            board[row][col] = AI
            evaluation, _ = minimax(board, False)
            board[row][col] = EMPTY
            if evaluation > best_eval:
                best_eval = evaluation
                best_move = (row, col)
    else:
        best_eval = math.inf
        for row, col in get_available_moves(board):
            board[row][col] = HUMAN
            evaluation, _ = minimax(board, True)
            board[row][col] = EMPTY
            if evaluation < best_eval:
                best_eval = evaluation
                best_move = (row, col)
    return best_eval, best_move

# Minimax with Alpha-Beta Pruning
def alpha_beta(board, is_ai_turn, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1, None
    elif winner == HUMAN:
        return -1, None
    elif winner == 'Draw':
        return 0, None

    best_move = None
    if is_ai_turn:
        best_eval = -math.inf
        for row, col in get_available_moves(board):
            board[row][col] = AI
            evaluation, _ = alpha_beta(board, False, alpha, beta)
            board[row][col] = EMPTY
            if evaluation > best_eval:
                best_eval = evaluation
                best_move = (row, col)
            alpha = max(alpha, best_eval)
            if beta <= alpha:
                break
    else:
        best_eval = math.inf
        for row, col in get_available_moves(board):
            board[row][col] = HUMAN
            evaluation, _ = alpha_beta(board, True, alpha, beta)
            board[row][col] = EMPTY
            if evaluation < best_eval:
                best_eval = evaluation
                best_move = (row, col)
            beta = min(beta, best_eval)
            if beta <= alpha:
                break
    return best_eval, best_move

# Compare performance of Minimax vs Alpha-Beta
def compare_algorithms():
    board = create_board()
    board[1][0] = HUMAN
    board[1][1] = AI
    board[1][2] = HUMAN

    print("Initial Board:")
    print_board(board)

    start_time = time.time()
    _, minimax_move = minimax(board, True)
    minimax_time = time.time() - start_time
    print("Minimax chose move:", minimax_move)
    print("Minimax time:", minimax_time, "seconds")

    start_time = time.time()
    _, alpha_beta_move = alpha_beta(board, True, -math.inf, math.inf)
    alpha_beta_time = time.time() - start_time
    print("Alpha-Beta Pruning chose move:", alpha_beta_move)
    print("Alpha-Beta time:", alpha_beta_time, "seconds")

compare_algorithms()
