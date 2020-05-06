# from "FILE NAME without ext"  import class (capital)
from square import Square
from constants import Constants
from pieces import *

class Board:

    playingBoard = []

    def init_board(self):

        x_square_names = ['a','b','c','d','e','f','g','h']
        
        self.playingBoard = [[Square(x_square_names[j]+str(i), 0) for i in range(1,9)] for j in range(8)]

        for i in range(8):
            self.playingBoard[i][1].updateSquare(Pawn(Constants.WHITE))
            self.playingBoard[i][6].updateSquare(Pawn(Constants.BLACK))
            

                
    def __init__(self):
        self.init_board()


b1 = Board()
b1.playingBoard[5][1].output()
b1.playingBoard[5][1].printPieceInfo()


    





