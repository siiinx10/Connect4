import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

#Create board
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board


def drop_piece(board, row, column, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
        
def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #check horizontal locations for the win
    #-3 for column because no way of getting winning at the last 3
    for col in range(COLUMN_COUNT -3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and  board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True


#main game loop
game_over = False
board = create_board()
turn = 0

while not game_over:
    #Ask Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6):"))

        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board,row,col,1)

            if winning_move(board, 1):
                print("Player 1 Wins!")

    #Ask for player 2 input
    else: 
        col = int(input("Player 2 enter your selection (0-6):"))
        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board,row,col,2)

    print_board(board)

    turn += 1
    turn = turn % 2
