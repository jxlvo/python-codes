import random

class Board():

    def __init__(self):
        self.lines = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    #Board layout
    def display(self):
        print("{}|{}|{}".format(self.lines[0], self.lines[1], self.lines[2]))
        print("{}|{}|{}".format(self.lines[3], self.lines[4], self.lines[5]))
        print("{}|{}|{}".format(self.lines[6], self.lines[7], self.lines[8]))

    def winner(self):
        
        #X wins
        if self.lines[0] == self.lines[1] == self.lines[2] == "X":
            return True
        elif self.lines[3] == self.lines[4] == self.lines[5] == "X":
            return True
        elif self.lines[6] == self.lines[7] == self.lines[8] == "X":
            return True
        elif self.lines[0] == self.lines[4] == self.lines[2] == "X":
            return True
        elif self.lines[2] == self.lines[4] == self.lines[6] == "X":
            return True
        elif self.lines[0] == self.lines[3] == self.lines[6] == "X":
            return True
        elif self.lines[1] == self.lines[4] == self.lines[7] == "X":
            return True
        elif self.lines[2] == self.lines[5] == self.lines[8] == "X":
            return True

        #O wins
        elif self.lines[0] == self.lines[1] == self.lines[2] == "O":
            return False
        elif self.lines[3] == self.lines[4] == self.lines[5] == "O":
            return False
        elif self.lines[6] == self.lines[7] == self.lines[8] == "O":
            return False
        elif self.lines[0] == self.lines[4] == self.lines[2] == "O":
            return False
        elif self.lines[2] == self.lines[4] == self.lines[6] == "O":
            return False
        elif self.lines[0] == self.lines[3] == self.lines[6] == "O":
            return False
        elif self.lines[1] == self.lines[4] == self.lines[7] == "O":
            return False
        elif self.lines[2] == self.lines[5] == self.lines[8] == "O":
            return False

        
    #Auto play
    def play(self):
        x = random.randint(0,8)
        y = random.randint(0,8)
        if self.lines[x] != "_":
            x = random.randint(0,8)
            self.lines[x] = "X"
        else:
            self.lines[x] = "X"
                
        if self.lines[y] != "_":
            y = random.randint(0,8)
            self.lines[y] = "O"
        else:
            self.lines[y] = "O"
        self.display()

board = Board()

for i in range(6):
    board.play()
    board.winner()
    print("")

    if board.winner() == True:
      print("X wins")
      break

    elif board.winner() == False:
      print("O wins")
      break

else: 
  print("Draw")
