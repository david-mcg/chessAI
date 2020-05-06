# from "FILE NAME without ext"  import class (capital)
from square import Square

from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook 
from pawn import Pawn

class Board:


    playingBoard = []

    def init_board(self):

        x_square_names = ['a','b','c','d','e','f','g','h']
        
        self.playingBoard = [[Square(x_square_names[j]+str(i), 0) for i in range(1,9)] for j in range(8)]

        for i in range(8):
            self.playingBoard[1][i].updateSquare(Pawn("bruce"))
                
    def __init__(self):
        self.init_board()


b1 = Board()
b1.playingBoard[1][2].output()


    





