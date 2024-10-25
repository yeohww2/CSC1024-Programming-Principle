print(' _______________________________________________________________ ')
print()
print()
print("╭(●｀∀´●)╯ Welcome to Tic-Tac-Toe WORLD ╰(●’◡’●)╮")
print()   
print(" _______________________________________________________________ ")
print()
print("ε=ε=ε= Please read the following instruction =ε=ε=┌(;￣◇￣)┘")
print()
print("The player who has obtained either three 'x' or 'o' in a row")
print('(either in horizontal, vertical or diagonal) is the WINNER!!! （●>∀<●）\n')
print(20*' ',"   Reference:    ") 
print(20*' ','  1  | 2  | 3    ')
print(20*' ',"  4  | 5  | 6    ")
print(20*' ',"  7  | 8  | 9    \n")


import random

def drawBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[2] == le and bo[5] == le and bo[8] == le) or 
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def inputPlayerLetter():
    letter = ''
    while letter not in ('X', 'O'):
        letter = input('Choose X or O ').upper()
    return ['X', 'O'] if letter == 'X' else ['O', 'X']

def makeMove(board, letter, move):
    if isSpaceFree(board, move):
        board[move] = letter
    else:
        raise Exception("makeMove: the field is not empty!")

def getComputerMove(board, computerLetter):
    playerLetter = 'O' if computerLetter == 'X' else 'X'
    
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on the next move, and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def getBoardCopy(board):
    return board[:]

def whoFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'human'
    
def isSpaceFree(board, move):
    return board[move] == ' '

def playerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Your turn to move (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = [i for i in movesList if isSpaceFree(board, i)]

    if possibleMoves:
        return random.choice(possibleMoves)
    return None

def isBoardFull(board):
    return all([not isSpaceFree(board, i) for i in range(1, 10)])

def playAgain():
    print('Wanna play again? (y or n)')
    return input().lower().startswith('y')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'human':
            drawBoard(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You are the winner !!!!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('No one wins!!! ')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You are the loser !!!!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('No one wins!!! ')
                    break
                else:
                    turn = 'human'

    if not playAgain():
        break
