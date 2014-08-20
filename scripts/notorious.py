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

def get_legal_moves():
	# figure out if I can get this from gnubg, otherwise, TODO: implement it
	moves = implement_me

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
((0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0), 
	(0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0))
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
