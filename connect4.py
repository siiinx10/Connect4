import numpy as np 
import pygame

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
	# Check horizontal locations for win
    #check horizontal locations for the win
    #-3 for column because no way of getting winning at the last 3
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True
    # Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True
               
    # Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

    

#main game loop
game_over = False
board = create_board()
turn = 0
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = ROW_COUNT +1  * SQUARESIZE #addition +1 row to create space to drop the pieces

size = (width, height)

screen = pygame.display.set_mode(size)

while not game_over:
    #Ask Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6):"))

        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board,row,col,1)

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True

    #Ask for player 2 input
    else: 
        col = int(input("Player 2 enter your selection (0-6):"))
        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board,row,col,2)

            if winning_move(board, 2):
                print("Player 2 Wins!")
                game_over = True

    print_board(board)

    turn += 1
    turn = turn % 2
