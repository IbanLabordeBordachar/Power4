cols = 7
rows = 6

# Créer une grille vide (liste de colonnes)
board = [[] for _ in range(cols)]

def display_symbol(cell):
    """Affichage coloré pour chaque joueur"""
    if cell == "R":
        return "\x1b[41m X \x1b[0m"  # Rouge joueur 1
    elif cell == "J":
        return "\x1b[43m 0 \x1b[0m"  # Jaune joueur 2
    else:
        return "   "  # Vide

def print_board(board, rows=6, cols=7):
    """Affiche la grille"""
    for r in reversed(range(rows)):
        row = []
        for c in range(cols):
            if r < len(board[c]):
                row.append(display_symbol(board[c][r]))
            else:
                row.append("   ")
        print("|" + "|".join(row) + "|")
    print("+---+---+---+---+---+---+---+")
    print(" 0   1   2   3   4   5   6")  # indices colonnes

def drop_piece(board, col, player):
    """Dépose un pion dans une colonne si possible"""
    if 0 <= col < cols and len(board[col]) < rows:
        board[col].append(player)
        return True
    else:
        return False  # colonne pleine ou invalide

def check_winner(board, player):
    """Vérifie si le joueur a gagné"""
    # Horizontal
    for r in range(rows):
        for c in range(cols - 3):
            if all(r < len(board[c+i]) and board[c+i][r] == player for i in range(4)):
                return True

    # Vertical
    for c in range(cols):
        for r in range(len(board[c]) - 3):
            if all(board[c][r+i] == player for i in range(4)):
                return True

    # Diagonale ↘
    for c in range(cols - 3):
        for r in range(rows - 3):
            if all(r+i < len(board[c+i]) and board[c+i][r+i] == player for i in range(4)):
                return True

    # Diagonale ↙
    for c in range(3, cols):
        for r in range(rows - 3):
            if all(r+i < len(board[c-i]) and board[c-i][r+i] == player for i in range(4)):
                return True

    return False

def is_full(board):
    """Vérifie si la grille est pleine"""
    return all(len(board[c]) == rows for c in range(cols))

# --- Boucle de jeu ---

if __name__ == '__main__' :
    print("Nom joueur 1")
    nom1 = input("")
    print("Nom joueur 2")
    nom2 = input("")

    # Liste des joueurs : (nom, symbole)
    players = [(nom1, "R"), (nom2, "J")]

    current = 0  # joueur courant

    while True:
        print_board(board)
        print(f"Joueur {players[current][0]} à vous !")
        
        try:
            col = int(input("Choisissez une colonne (0-6) : "))
        except ValueError:
            print("Entrée invalide, entrez un nombre entre 0 et 6.")
            continue

        if not drop_piece(board, col, players[current][1]):
            print("Colonne pleine ou invalide, choisissez-en une autre.")
            continue

        # Vérifier si le joueur a gagné
        if check_winner(board, players[current][1]):
            print_board(board)
            print(f"Le joueur {players[current][0]} a gagné !")
            break

        # Vérifier si la grille est pleine
        if is_full(board):
            print_board(board)
            print("Égalité !")
            break

        # Changer de joueur
        current = 1 - current
