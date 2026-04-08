from random import randrange

# Plateau initial
board = [[str(3*i + j + 1) for j in range(3)] for i in range(3)] #initialisatio du plateau
board[1][1] = 'X'  # premier coup de l'ordinateur

# Afficher le plateau
def display_board(board):
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i < 2: #barre horizontale
            print('--+---+--')

# Liste des cases libres
def free_fields(board):
    return [(i,j) for i in range(3) for j in range(3) if board[i][j] not in ('X','O')] # retourne la liste de tuple
# des 

# Coup de l'utilisateur
def user_move(board):
    while True:
        try:
            res = int(input("Votre coup (1-9) : "))
            row, col = (res-1)//3, (res-1)%3
            if board[row][col] in ('X','O'):
                print("Case occupée, réessayez")
            else:
                board[row][col] = 'O'
                break
        except:
            print("Entrée invalide, réessayez")

# Vérifier victoire
def victory(board, sign):
    # Vérifier les lignes
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True

    # Vérifier les colonnes
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True

    # Vérifier la diagonale principale
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    # Vérifier la diagonale secondaire
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    # Si aucune victoire
    return False # Coup de l'ordinateur

def computer_move(board):
    free = free_fields(board)  # récupère toutes les cases libres
    if len(free) > 0:          # s'il y a au moins une case libre
        index = randrange(len(free))  # choisit un indice aléatoire
        row, col = free[index]        # récupère les coordonnées
        board[row][col] = 'X'         # place le X de l'ordinateur

# Boucle principale
while True:
    display_board(board)
    
    if victory(board, 'X'):
        print("Ordinateur gagne !")
        break
    
    if not free_fields(board):
        print("Match nul !")
        break
    
    user_move(board)
    
    if victory(board, 'O'):
        display_board(board)
        print("Vous gagnez !")
        break
    
    if not free_fields(board):
        display_board(board)
        print("Match nul !")
        break
    
    computer_move(board)
