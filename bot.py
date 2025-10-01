from jeu import *

def copy_board(board) :
    new_board = []    
    for col in board :
        new_col = col.copy() 
        new_board.append(new_col)
    return new_board

def score_window(window, player):
    opponent = "J" if player == "R" else "R"
    score = 0
    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(" ") == 1:
        score += 10
    elif window.count(player) == 2 and window.count(" ") == 2:
        score += 5

    if window.count(opponent) == 3 and window.count(" ") == 1:
        score -= 80  # bloquer l’adversaire est très important
    return score

def evaluate_board(board):
    """Donne une valeur heuristique à la grille"""
    score = 0
    player = "R"
    
    # Score colonnes centrales (important dans Puissance 4)
    center = cols // 2
    center_count = board[center].count(player)
    score += center_count * 3

    # Horizontal
    for r in range(rows):
        row = []
        for c in range(cols):
            if r < len(board[c]):
                row.append(board[c][r])
            else:
                row.append(" ")
        for c in range(cols - 3):
            window = row[c:c+4]
            score += score_window(window, player)

    # Vertical
    for c in range(cols):
        col = board[c] + [" "] * (rows - len(board[c]))
        for r in range(rows - 3):
            window = col[r:r+4]
            score += score_window(window, player)

    # Diagonales ↘ et ↙
    for c in range(cols - 3):
        for r in range(rows - 3):
            window = [ board[c+i][r+i] if r+i < len(board[c+i]) else " " for i in range(4) ]
            score += score_window(window, player)

    for c in range(3, cols):
        for r in range(rows - 3):
            window = [ board[c-i][r+i] if r+i < len(board[c-i]) else " " for i in range(4) ]
            score += score_window(window, player)

    return score


def minmax(board, depth, is_maximizing):
    if check_winner(board, "R"):
        return 1_000_000
    if check_winner(board, "J"):
        return -1_000_000
    if is_full(board):
        return 0
    if depth == 0:
        return evaluate_board(board)  # heuristique intermédiaire

    if is_maximizing:  # Bot = "R"
        best_score = -float("inf")
        for c in range(cols):
            if len(board[c]) < rows:
                new_board = copy_board(board)
                drop_piece(new_board, c, "R")
                score = minmax(new_board, depth-1, False)
                best_score = max(score, best_score)
        return best_score
    else:  # Joueur = "J"
        best_score = float("inf")
        for c in range(cols):
            if len(board[c]) < rows:
                new_board = copy_board(board)
                drop_piece(new_board, c, "J")
                score = minmax(new_board, depth-1, True)
                best_score = min(score, best_score)
        return best_score


def best_move(board, depth=4):
    """
    Retourne l'indice de la colonne pour le meilleur coup pour le bot ("R")
    """
    best_score = -float('inf')
    move = None
    for c in range(cols):
        if len(board[c]) < 6:
            new_board = copy_board(board)
            drop_piece(new_board, c, "R")
            score = minmax(new_board, depth-1, False)
            if (score > best_score ):
                best_score = score
                move = c
    return move
