import random as rd
from time import sleep
class Board:
    board = '''
               1 | 2 | 3
             -------------
               4 | 5 | 6
             -------------
               7 | 8 | 9
            '''
    def __init__(self):
      #the suffix i indicates the index while the variables without the suffix indicate the values at that index
        self.onei = Board.board.index("1")
        self.one = Board.board[self.onei]
        self.twoi = Board.board.index("2")
        self.two = Board.board[self.twoi]
        self.threei = Board.board.index("3")
        self.three = Board.board[self.threei]
        self.fouri = Board.board.index("4")
        self.four = Board.board[self.fouri]
        self.fivei = Board.board.index("5")
        self.five = Board.board[self.fivei]
        self.sixi = Board.board.index("6")
        self.six = Board.board[self.sixi]
        self.seveni = Board.board.index("7")
        self.seven = Board.board[self.seveni]
        self.eighti = Board.board.index("8")
        self.eight = Board.board[self.eighti]
        self.ninei = Board.board.index("9")
        self.nine = Board.board[self.ninei]
        self.diag = [self.one, self.nine, self.five, self.three, self.seven]
        self.vert = [self.one, self.four, self.seven, self.two, self.five, self.eight, self.three, self.six, self.nine]
        self.horiz = [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]
        self.edges = [self.two, self.four, self.six, self.eight]
        self.diags = [self.one, self.three, self.seven, self.nine]
        
#playing a position
    def play(self, pos, elt):
        Board.board = Board.board.replace(pos, elt)
    def win(self):
        global board
        global draw
        global gameover
        global winner
        #checking the diagonals
        if (all([pos=="X" for pos in self.diag[:3]]) or all([pos=="O" for pos in self.diag[:3]])) or (all([pos=="X" for pos in self.diag[2:]]) or all([pos =="O" for pos in self.diag[2:]])):
            gameover = True
            if gameover:
                if self.five == "X":
                    if player1.choice == "X": 
                        winner = player1
                    else: 
                        winner = player2
                else: 
                    if player1.choice == "O": 
                    
                        winner = player1
                    else: 
                    
                        winner = player2
        #checking the verticals
        elif (all([pos=="X" for pos in self.vert[:3]]) or all([pos=="O" for pos in self.vert[:3]])) or (all([pos=="X" for pos in self.vert[3:6]]) or all([pos=="O" for pos in self.vert[3:6]])) or (all([pos=="X" for pos in self.vert[6:]]) or all([pos=="O" for pos in self.vert[6:]])):
            gameover = True
            if gameover:
                if "X" in (self.one, self.two, self.three):
                    if player1.choice == "X": 
                        winner = player1
                    else: 
                        winner = player2
                else: 
                    if player1.choice == "O": 
                        winner = player1
                    else: 
                        winner = player2
        #checking the horizontals
        elif (all([pos=="X" for pos in self.horiz[:3]]) or all([pos=="O" for pos in self.horiz[:3]])) or (all([pos=="X" for pos in self.horiz[3:6]]) or all([pos=="O" for pos in self.horiz[3:6]])) or (all([pos=="X" for pos in self.horiz[6:]]) or all([pos=="O" for pos in self.horiz[6:]])):
            gameover = True
            if gameover:
                if "X" in (self.one, self.four, self.seven):
                    if player1.choice == "X":
                        winner = player1
                    else:
                        winner = player2
                else:
                    if player1.choice == "O": 
                        winner = player1
                    else:
                        winner = player2
        #checking for a draw
        elif all([self.diag + self.edges in ("X", "O")]):
            gameover = True
            draw = True
            print("\t\tDRAW!!\nIt seems you both are equally matched... you might require further battles to determine the victor :}")
class Computer:
    def __init__(self):
        self.choice = ""
        self.pos = 0
    def easy(self):
        pass
    def medium(self):
        pass
    def asian(self):
        pass
class Player:
    def __init__(self):
        self.choice = ""
        self.chances = 3
def Multiplayer(char):
    global winner
    print(f"Player1 has chosen '{char}' as their character!")
    opt1 = "X"
    opt2 = "O"
    if char == "X":
        player2.choice = opt2
        print(f"Player2 will be using '{opt2}' as '{opt1}' is already taken")
    else:
        print(f"Player2 will be using '{opt1}' as '{opt2}' is already taken")
        player2.choice = opt1
    print("Let the games begin!!!!")
    sleep(1)
    play_M()
    if winner == player1: w = "Player1"
    elif winner == player2: w = "Player2"
    print(f"\t\t{w} has won the game!\ngameover...")
    sleep(2)
#multiplayer play scenario
def play_M():
    global gameover
    global board
    global draw
    print("Player1 shall begin first")
    #if player2 is Computer:
    print("....")
    sleep(0.5)
    choice = input("Or would Player2 prefer to begin first?[y/n]\n: ").lower()
    while choice not in ("y", "n"):
        choice = input("Oops! you haven't entered either 'y' or 'n'\n Select the right option: ").lower()
    if choice == "y":
        x = "Player2"
        y = "Player1"
    else:
        x = "Player1"
        y = "Player2"
    while not gameover:
        print(board.board)
        pos = int(input(f"{x} select the number of the postion you want to play: "))
        while pos not in range(1,10):
            pos = int(input("Oops! you haven't entered a valid position\n Select a valid option: "))
        board.play(str(pos), player1.choice)
        print(board.board)
        board.win()
        if draw:
            choice = input("play again?[y/n]: ").lower()
            while choice not in ("y", "n"):
                choice = input("Oops! you didn't select 'y' or 'n'. Select the right option to advance\n: ").lower()
            if choice == "y":
                gameover = False
                board = Board()
                continue
            else: break
        #ends the game if the condition is met before the opponent plays
        elif gameover: break
        pos = int(input(f"{y} select the number of the position you want to play: "))
        while pos not in range(1,10):
            pos = int(input("Oops! you haven't entered a valid position\n Select a valid option: "))
        board.play(str(pos), player2.choice)
        board.win()
        if draw:
            choice = input("play again?[y/n]: ").lower()
            while choice not in ("y", "n"):
                choice = input("Oops! you didn't select 'y' or 'n'. Select the right option to advance\n: ").lower()
            if choice == "y":
                gameover = False
                board = Board()
                continue
            else: break
        elif gameover: break

def Singleplayer(char):
    print(f"Player1 has chosen '{char}' as their character!")
    print("[Player2 is now the computer]")
    sense = input("\t\t__[DIFFICULTY]__\n\t\t[Select a number]\n\t1. Easy\n\t2. Medium\n\t3. ASIAN\n\t:")
    while sense not in (1, 2, 3):
        sense = input("Oops! you haven't entered a valid option\n Select a valid option: ")
    if sense == 1:
        player2.easy()
    elif sense == 2:
        player2.medium()
    else:
        player2.asian()
    

#MAIN GAME
gameover = False
draw = False
winner = None
player1 = Player()
board = Board()
print(type(board.edges))
print("Welcome to Tic")
sleep(1)
print("Tac")
sleep(1)
print("Toe!!")
print(board.board)
sleep(1)
print("A little bit of info before you begin!\nThe game is played like a normal Tic Tac Toe game with a player winning if three of their characters line up consecutively. If that condition is fufilled, the game is over.\n\tThe game will be played by selecting your character, and then selecting the position you want to play on the board and then pressing enter! Simple isn't it?\nSelect Singleplayer if you want to go against the computer or Multiplayer if you are playing with a friend. Goodluck!!")
sleep(2.5)
mode = int(input("\t\t__[MODE]__\n\t1. Singleplayer\n\t2. Multiplayer\n\t:"))
while mode not in (1, 2):
    mode = input("Oops! you haven't entered either '1' or '2'\n Select the right option: ")
player1.choice = input("Select your character: X or O\n:").upper()
while player1.choice not in ("X", "O"):
    player1.choice = input("Oops! you haven't entered either 'X' or 'O'\n Select the right option: ").upper()
if mode == 1:
    player2 = Computer()
    Singleplayer(player1.choice)   
elif mode == 2:
    player2 = Player()
    Multiplayer(player1.choice)
    
