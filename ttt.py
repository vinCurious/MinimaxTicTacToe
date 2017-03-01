# ttt.py
# Author: Vinay More, RIT, Sept.2016
def printBoard(board):
    """printBoard function prints the board grid."""
    element=0
    for i in range(0,3):
        for j in range(0,3):
            print(str(board[element])+" ",end='')
            element=element+1
        print("")

def isGameOver(board):
    """isGameOver returns whether game is over or not by looking at board state"""
    #Checks whether any one won or not
    if whoWon(board)=='X' or whoWon(board)=='O':
        return True
    #checks whether board state is in draw state
    if isDraw(board):
        return True
    #otherwise return false
    return False

def whoWon(a):
    """whoWon function checks whether any user won it or not and returns user marker"""
    if (a[0]==a[1] and a[1]==a[2]):
        return a[0]
    elif (a[3]==a[4] and a[4]==a[5]):
        return a[3]
    elif (a[6]==a[7] and a[7]==a[8]):
        return a[6]
    elif (a[0]==a[3] and a[3]==a[6]):
        return a[0]
    elif (a[1]==a[4] and a[4]==a[7]):
        return a[1]
    elif (a[2]==a[5] and a[5]==a[8]):
        return a[2]
    elif (a[0]==a[4] and a[4]==a[8]):
        return a[0]
    elif (a[2]==a[4] and a[4]==a[6]):
        return a[2]
    return False

def piececanbePlayed(board):
    """piececanbePlayed function checks whether at least one open position is left on the board or not"""
    for i in range(0,9):
        if board[i]!='X' and board[i]!='O':
            return True
    return False

def isDraw(board):
    """isDraw function checks whether any user won it or not and returns user marker"""
    if(piececanbePlayed(board)):
        return False
    return True

def playHuman(board):
    """playHuman function represents a human player and plays the move based on user's input"""
    move= int(input("Player1's Turn: "))
    board[move-1]='X'
    return board

def playAI(board,minimax):
    """playAI function reprsents AI player and used algorithm based on the minimax boolean value"""
    #if regular minimax algorithm is to be used
    if minimax==True:
        move=int(MiniMaxDecision(board))
    else:
        #if minimax algorithm with alphabeta pruning is to be used
        move=int(alphabetaDecision(board))
    print("Player AI played at "+str(move+1))
    board[move]='O'
    return board

def makemove(board,move,player):
    """makemove function just puts the player marker on the board"""
    board[move]=player
    return board

def MiniMaxDecision(board):
    """MiniMaxDecision function is helper function to handle maxval(board) and minval(board) function for minimax Algorithm"""
    v,i = maxval(board)
    print("No. of search tree nodes Minimax: "+str(Solution.minmaxcounter))
    return getOpenLocations(board)[i]

def maxval(board):
    """maxval function of minimax algorithm which maximizes payoff against optimal component"""
    result=[]
    #Terminal tests
    if isGameOver(board):
        if whoWon(board)=='X':
            return -1,1
        elif isDraw(board):
            return 0,1
        elif whoWon(board)=='O':
            return 1,1
    v = -9
    for move in getOpenLocations(board):
        board=makemove(board,move,'O')
        #counter to count search tree nodes
        Solution.minmaxcounter=Solution.minmaxcounter+1
        a,i=minval(board)
        v=max(v,a)
        result.append(v)
        board=makemove(board,move,str(move+1))
    return max(result),result.index(max(result))

def minval(board):
    """minval function of minimax algorithm"""
    result=[]
    #Terminal tests
    if isGameOver(board):
        if whoWon(board)=='X':
            return -1,1
        elif isDraw(board):
            return 0,1
        elif whoWon(board)=='O':
            return 1,1
    v = 9
    for move in getOpenLocations(board):
        board=makemove(board,move,'X')
        #counter to count serach tree nodes
        Solution.minmaxcounter=Solution.minmaxcounter+1
        a,i=maxval(board)
        v=min(v,a)
        result.append(v)
        board=makemove(board,move,str(move+1))
    return min(result),result.index(min(result))

def alphabetaDecision(board):
    """alphabetaDecision function is helper function to handle alphabetaMaxval(board,a,b) and alphabetaMinval(board,a,b) function for minimax Algorithm with alphabeta pruning"""
    v,i=alphabetaMaxval(board,-9,9)
    print("No. of search tree nodes alphabetpruning: "+str(Solution.alphabetacounter))
    return getOpenLocations(board)[i]

def alphabetaMaxval(board,a,b):
    """alphabetaMaxval function of minimax algorithm with alphabeta pruning indentifies best payoff found so far for the max player"""
    result=[]
    #Terminal tests
    if isGameOver(board):
        if whoWon(board)=='X':
            return -1,1
        elif isDraw(board):
            return 0,1
        elif whoWon(board)=='O':
            return 1,1
    v=-9
    for move in getOpenLocations(board):
        board=makemove(board,move,'O')
        #counter to count serach tree nodes
        Solution.alphabetacounter=Solution.alphabetacounter+1
        tmp,j = alphabetaMinval(board,a,b)
        v=max(v,tmp)
        result.append(v)
        board=makemove(board,move,str(move+1))
        v=max(result)
        #prune path to max nodes using beta i.e. b
        if v >=b:
            return v,result.index(v)
        a=max(a,v)
    return v,result.index(v)

def alphabetaMinval(board,a,b):
    """alphabetaMinval function of minimax algorithm with alphabeta pruning indentifies smallest payoff found for max player"""
    result=[]
    #Terminal tests
    if isGameOver(board):
        if whoWon(board)=='X':
            return -1,1
        elif isDraw(board):
            return 0,1
        elif whoWon(board)=='O':
            return 1,1
    v=9
    for move in getOpenLocations(board):
        board=makemove(board,move,'X')
        #counter to count search tree nodes
        Solution.alphabetacounter=Solution.alphabetacounter+1
        tmp,j = alphabetaMaxval(board,a,b)
        v=min(v,tmp)
        result.append(v)
        board=makemove(board,move,str(move+1))
        v=min(result)
        #prune path to min nodes using alpha i.e a
        if v <=a:
            return v,result.index(v)
        b=min(b,v)
    return v,result.index(v)

def getOpenLocations(board):
    """getOpenLocations gets the board state and returns all open positions on the board"""
    return [int(x)-1 for x in board if x!='X' and x!='O']

def playGame(board,minimax):
    """playGame function takes board and True or False value to inform whether to use minimax algorithm or minimax algorithm with aplhabeta pruning."""
    while(True):
        #Terminating conditions
        if  whoWon(board)=='X':
            print("Player1 wins")
            break
        elif whoWon(board)=='O':
            print("AI wins")
            break
        elif isDraw(board):
            print("Game Drawn")
            break
        else:
            #Human player call
            board=playHuman(board)
            printBoard(board)

            if not isGameOver(board):
                #AI player call
                board=playAI(board,minimax)
                printBoard(board)

# Main program.
# This program initiates two games one after the other
# Human player first plays with regular MiniMax Algorithm and then with MiniMax algorithm with AlphaBeta pruning
def main():
    print("--------TicTacToe----------")
    print("-------Using MiniMax-------")
    #Preparing board for first game
    board1=range(1,10)
    board1=[str(x) for x in board1]
    printBoard(board1)
    #first game call
    playGame(board1,True)

    print("-------Using Alpha Beta Pruning-------")
    #Preparing board for second game
    board2=range(1,10)
    board2=[str(x) for x in board2]
    printBoard(board2)
    #second game call
    playGame(board2,False)


class Solution:
    """Class for storing two static counters to count search tree nodes"""
    #Counter of search tree nodes in regular MiniMax Algorithm
    minmaxcounter=0

    #Counter of search tree nodes in MiniMax Algorithm with AlphaBeta Pruning
    alphabetacounter=0

main()