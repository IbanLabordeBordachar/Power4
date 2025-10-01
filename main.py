from jeu import *
from bot import *


print("Si vous voulez commencer, écrivez Oui ")
print("Sinon, écrivez Non ")

reponse = str(input(""))
if ( reponse == "Non" ) or ( reponse == "non") :
    while True : 
    # Tour bot
        move = best_move(board)
        drop_piece(board, move, "R")
        if check_winner(board, "R"):
            print_board(board)
            print("Bot a gagné !")
            break
        if is_full(board):
            print_board(board)
            print("Égalité !")
            break
        print_board(board)
    # Tour joueur 
        move = int(input("Ton coup (0-6): "))
        drop_piece(board, move, "J")

        if check_winner(board, "J"):
            print_board(board)
            print("Tu as gagné !")
            break
        if is_full(board):
            print_board(board)
            print("Égalité !")
            break
elif ( reponse == "Oui") or ( reponse =="oui") : 
    while True:
        print_board(board)
        # Tour joueur 
        move = int(input("Ton coup (0-6): "))
        drop_piece(board, move, "J")

        if check_winner(board, "J"):
            print_board(board)
            print("Tu as gagné !")
            break
        if is_full(board):
            print_board(board)
            print("Égalité !")
            break
        # Tour bot
        move = best_move(board)
        drop_piece(board, move, "R")
        if check_winner(board, "R"):
            print_board(board)
            print("Bot a gagné !")
            break
        if is_full(board):
            print_board(board)
            print("Égalité !")
            break
        print_board(board)
