import gnubg
import random

print "Hello, world"

def new(opponent_type="gnubg"):
	if opponent_type == "human":
		gnubg.command("set player 0 human")
		gnubg.command("new session")
	elif opponent_type == "gnubg":
		gnubg.command("set player 0 gnubg")
		gnubg.command("new session")


#checks legality for a die value at a board location num given a board (assuming we are player 1)
def get_moves_from_pos(movelist,board,dice,numdice,numpos):
	# if we have reached the end of the board traversal, or if we have reached the end of our dice traversal
	# then return to previous level of recursion
	if numpos <= 0 or numdice > len(dice):
		return movelist
	else:
		# if there are pips at this position
		if board[1][numpos] != 0:
			# can we take them off the board? (are all pieces in inner board)
			canTakeOff=bool(not sum(board[1][7:24]))
			if numpos - d <= 0:
				# if yes and if we are trying to do that, take them off
				# LATER: DISCARD MOVES THAT TAKE OFF BUT ARE NOT ALLOWED
				if canTakeOff:
					move = (numpos, numpos - d)
					board[1][numpos] -= 1
				# iterate forwards in dice but not position
					movelist[move]=get_moves_from_pos(movelist[move],board,dice,numdice+1,24)
				else:
					return get_moves_from_pos(movelist,board,dice,numdice,numpos-1)
			else:
				# check no opponent blockage, if not, create move and update board
				if board[0][24-(numpos - d)] < 2:
					move = (numpos, numpos - d)
					board[1][numpos] -= 1
					board[1][numpos - d] += 1
				movelist[move] = get_moves_from_pos(movelist[move],board,dice,numdice+1,24)
		else:
			#iterate through position if you can't make a move!
			return get_moves_from_pos(movelist,board,dice,numdice,numpos-1)
		

def get_legal_moves():
	# TODO: implement checking if piece is on bar, also if highest roll is not available
	posinfo = gnubg.posinfo()
	dice = posinfo['dice']
	board = gnubg.board()
	# check for doubles case
	isDouble = dice[0] == dice[1]
	#can the board take off pieces? (check after each move)
	canTakeOff = bool(not sum(board[1][7:24]))

	for i in range(board[1]):
		num_position = board[1][i]
		if num_position != 0:
			for d in dice:
				if is_legal(board,p,d):
					move_one = 
					return

	if board[1][24] in player_positions != 0:
		# bar stuff, implement

	# if doubles, 24/1(3) (5/1)

def random_move():
	moves = get_legal_moves()
	return random.choice(moves)

def smart_move():
	moves = get_legal_moves()
	# this might be a while

'''
dir(gnubg):
[
	'__doc__', 
	'__name__', 
	'__package__', 
	'board', 
	'cfevaluate', 
	'command', 
	'cubeinfo', 
	'dicerolls', 
	'eq2mwc', 
	'eq2mwc_stderr', 
	'errorrating', 
	'evalcontext', 
	'evaluate', 
	'findbestmove', 
	'gnubgid', 
	'hint', 
	'luckrating', 
	'match', 
	'matchchecksum', 
	'matchid', 
	'met', 
	'movetupletostring', 
	'mwc2eq', 
	'mwc2eq_stderr', 
	'navigate', 
	'nextturn', 
	'parsemove', 
	'posinfo', 
	'positionbearoff', 
	'positionfrombearoff', 
	'positionfromid', 
	'positionfromkey', 
	'positionid', 
	'positionkey', 
	'rolloutcontext', 
	'updateui'
]

>>> gnubg.board()
(2 = gnubg.board()[0][23] = gnubg.board()[1][0])
((0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0), 
	(0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0))
>>> gnubg.posinfo()
{'turn': 1, 'resigned': 0, 'gamestate': 1, 'dice': (1, 2), 'doubled': 0}
'''


'''
COMMANDS:

accept         	Accept a cube or resignation
agree          	Agree to a resignation
analyse        	Run analysis
annotate       	Record notes about a game
end            	Automatically make plays
beaver         	Synonym for `redouble'
calibrate      	Measure evaluation speed, for later time estimates
clear          	Clear information
cmark          	Mark candidates
copy           	Copy current position to clipboard
decline        	Decline a resignation
dicerolls      	Generate a list of rolls
double         	Offer a double
drop           	Decline an offered double
eq2mwc         	Convert normalised money equity to match winning chance
eval           	Display evaluation of a position
exit           	Leave GNU Backgammon
export         	Write data for use by other programs
external       	Make moves for an external controller
first          	Goto first move or game
help           	Describe commands
hint           	Give hints on cube action or best legal moves
invert         	invert match equity tables, etc.
import         	Import matches, games or positions from other programs
list           	Show a list of games or moves
load           	Read data from a file
move           	Make a backgammon move
mwc2eq         	Convert match winning chance to normalised money equity
new            	Start a new game, match or session
next           	Step ahead within the game
pass           	Synonym for `drop'
play           	Force the computer to move
previous       	Step backward within the game
quit           	Leave GNU Backgammon
redouble       	Accept the cube one level higher than it was offered
reject         	Reject a cube or resignation
relational     	Log matches to an external relational database
resign         	Offer to end the current game
roll           	Roll the dice
rollout        	Have gnubg perform rollouts of the current position.
save           	Write data to a file
set            	Modify program parameters
show           	View program parameters
swap           	Swap players
take           	Agree to an offered double
?              	Describe commands
'''
