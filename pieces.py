class Piece :
    def __init__(self, colour):
        self.colour = colour




class King (Piece):

    name = "King"

    def __init__(self, colour):
        print(" ")

class Pawn (Piece):
    
    def __init__(self,colour):
        super().__init__(colour)
        self.name = "Pawn"
        

class Queen (Piece):
    def __init__(self):
        print("hello")

class Bishop (Piece):
    def __init__(self):
        print("hello")

class Knight (Piece):
    def __init__(self):
        print("hello")

class Rook (Piece):
    def __init__(self):
        print("hello")

