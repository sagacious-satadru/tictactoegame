import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

# defining the width and height of our game window (setting both to 600 pixels)
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT) # A tuple consisting of the Width as the 1st element and and the Height as
# the 2nd element
CIRCLE = pygame.image.load('circle.png')
CROSS = pygame.image.load('x.png') # the image func helps us load an image from the computer
 
# we have used the constants ROWS = 3 and COLUMNS = 3 to specify the dimensions of the 2D array that'll 
# be used to represent our tic tac toe board
# the numpy zeros method helps create an array of the specified dimensions, filled with 0s

# Setting the colour of the board:-
WHITE = (255,255,255) # The RGB code for the color white
# Setting the color of the lines on the board:-
BLACK = (0,0,0)
# a colour for the winner
RED = (255,0,0)
BLUE = (0,0,255)



# now we'll create a function such that 1 will represent player 1s mark and 2 will rep player 2's mark
def mark(row,col, player):
	board[row][col] = player
	# the func takes the 3 arguments, i.e the row and column chosen by the player and the mark chosen
	# which can be either 1 or 2 (O or X)
	# inside the func the mark will be assigned to the corresponding board position/coordinates

# a func to check whether the chosen coordinates/position on the board is empty or not
def is_valid_mark(row, col):
	return board[row][col] == 0 # returns true if the selected square, i.e the coords of the selected square
	# are of a square that's empty(=0), o/w returns false

# a func to check whether all the squares on the board have been filled or not. We'll be requiring this
# function to check later if all the squares have been filled, and if yes, then restart the game
def is_board_full():
	for c in range(COLUMNS):
		for r in range(ROWS):
			if board[r][c] == 0: # if even 1 square on the board is 0, i.e empty then that means the 
			# board is not full, hence return False
				return False
	return True
def draw_board():
	# for each of player 1's moves we'll mark it with a circle O
	# and for each of player 2's moves we'll mark it with a cross X
	for c in range(COLUMNS):
		for r in range(ROWS):
			if board[r][c]==1:
				window.blit(CIRCLE,((c*200)+50,(r*200)+50))
			elif board[r][c]==2:
				window.blit(CROSS,((c*200)+50,(r*200)+50))
				# we import the image of the circle using the blit()
				# it takes 2 arguments, the 1st one being the image that we wish to import 
				# and the 2nd one being a tuple consisting of the x & y coords of where we want to 
				# import the image. The x coord here = current column number * 200(=the sq size) + 50(=offset)
				# the offset is to make the image centered (for both x and y coord the offset serves the same purpose)
				# The y coord here = current row number * 200(=the sq size) + 50(=offset)
	pygame.display.update()



# the func takes 5 arguments -> the window that we want to draw in, the color that we want to use,
# the starting position, the ending position and the width of the line
# our first horizontal line starts at (200,0) to (200,600)
def draw_lines():
	pygame.draw.line(window,BLACK,(200,0),(200,600),10)
	pygame.draw.line(window,BLACK,(400,0),(400,600),10)
	pygame.draw.line(window,BLACK,(0,200),(600,200),10)
	pygame.draw.line(window,BLACK,(0,400),(600,400),10)

def is_winning_move(player):
	if player == 1:
		# announcement = "Player 1 won"
		winning_color = BLUE # blue corresponds to player 1
	else:
		# announcement = "Player 2 Won"
		winning_color = RED # red corresponds to player 2
	for r in range(ROWS):
		# this loop goes through each square starting from the 1st row and all the way upto the 3rd row
		# which is the last row
		# Horizontal check :-
		if board[r][0] == player and board[r][1] == player and board[r][2] == player:
			# print(announcement)
			pygame.draw.line(window, winning_color, (10,(r*200) + 100 ), (WIDTH-10, (r*200) + 100),10)
			# the starting posn for the horizontal line that we're drawing will be an offset of 10 for the x posn
			# and the current row * 200(=sqaure size) + offset to make the line start at the center
			# the ending posn will be all the way to the other side, i.e WIDTH-10 and the y posn would be the 
			# the same since the line is horizontal
			return True # if any row containes all squares filled with the same symbol then that would 
			# mean that a certain player has won, i.e the situation would be like X X X or O O O
	# Vertical check :-
	for c in range(COLUMNS):
		if board[0][c] == player and board[1][c] == player and board[2][c] == player:
			# print(announcement)
			pygame.draw.line(window, winning_color, ( (c*200) + 100, 10), ((c*200)+100,HEIGHT-10), 10)  
			return True
	# Positive diagonal check :-
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
			# print(announcement)
			pygame.draw.line(window, winning_color, (10, 10), (590, 590), 10)
			return True
	# -ve diagonal check :-
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
			# print(announcement)
			pygame.draw.line(window, winning_color, (590,10), (10,590), 10 )
			return True


board = np.zeros((ROWS,COLUMNS))

# print(board)
# mark(1,0,2)
# print()
# print(is_valid_mark(1,0))

# we'll need a game loop variable to check whether the game is still running or not
game_over = False
Turn = 0

pygame.init()

# Creating the game window with Pygame
window = pygame.display.set_mode(SIZE) # this function will create a display surface

# Now giving a title to our game window :-
pygame.display.set_caption("Tic Tac Toe") # the func set_caption() is used to set/change the title of the
# window to the string argument

# Filling the window with white color
window.fill(WHITE)
draw_lines()
pygame.display.update() # the update() is responsible for making the changes made to the window to 
# take effect and refreshes it everytime update() is called. REMEMBER always call update() after making
# any changes to the window display

pygame.time.wait(2000) # the wait() is used as a delay. In other words it makes our screen hang for 
# 2000ms (the argument passed here)

# drawing the lines on the white board/window to make a 3x3 grid of 9 squares

# Rememeber that pygame is an event based module that can listen to the player's actions such
# as mouse clicks etc.

while not game_over:
	for event in pygame.event.get():
		# we need to termainate our game when the X button is clicked on
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(event.pos) # the pos attribute lets us know the position of the mouse click
			# on the window

			# we need a way to alternate b/w the 2 players turns
			if Turn % 2 == 0:
				#Player 1
				# row = int(input("Player 1 : Choose row number (0,2) : "))
				row = math.floor(event.pos[1]/200)
				col = math.floor(event.pos[0]/200)
				# col = int(input("Player 1 : Choose column number (0,2) : "))
				if is_valid_mark(row,col):
					mark(row,col,1)
					if is_winning_move(1):
						game_over = True
				else:
					Turn -= 1
			else:
				# Player 2
				# row = int(input("Player 2 : Choose row number (0,2) : "))
				# col = int(input("Player 2 : Choose column number (0,2) : "))
				row = math.floor(event.pos[1]/200)
				col = math.floor(event.pos[0]/200)
				if is_valid_mark(row,col):
					mark(row,col,2)
					if is_winning_move(2):
						game_over = True
				else:
					Turn -= 1

			Turn += 1
			print(board)
			draw_board()
	if is_board_full(): # so that the game can restart when the board is full or a tie happens
		game_over = True

	if game_over==True:
		print("Game Over")
		# to make the game restart after one of the players win
		pygame.time.wait(2000) # to create a delay of 2000ms before the next round starts
		board.fill(0) # resetting our board to 0s
		window.fill(WHITE) # refilling the board with white color
		draw_lines()  # draw the lines and the board using our funcs 
		draw_board() # draw the board again afrsh (/freshly)
		game_over = False # resetting the game variable to false so that the game loop can start all over again
		pygame.display.update() 