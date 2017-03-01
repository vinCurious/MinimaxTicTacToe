# MinimaxTicTacToe
Implementation of Minimax algorithm with alpha beta pruning for Tic-Tac-Toe game
--------------------------------------------------------------------------------------

Files in this directory:

ttt.py:  	TicTacToe game with regular Minimax and Minimax with alphabeta pruning algorithms implemented.
output.txt: Two complete game output with the states of the game board doing the game, and report the number 
			of search tree nodes generated for each move by the computer, using 1) regular Minimax, and 
			2) Minimax using alpha-beta pruning
			
How to run the game:
	1. Go to ttt.py
	2. In main function initialize the boards for both algorithms according to your requirement and run the ttt.py file 

Interpretations:
	1. The output file shows that the pruning does not change the decision of the moves from Minimax algorithm.
	   The sequence of the moves suggested by both the algorithms was exact same.
	2. Minimax algorithm generates search tree nodes around 65000 and with alpha beta pruning we can exponentially lower that
	   down to around 3000.
	3. If moves are ordered properly then effectiveness of pruning can be improved.
