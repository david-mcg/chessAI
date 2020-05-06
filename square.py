class Square:

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    

    def updateSquare(self, new_piece):
        self.piece = new_piece


    def printPieceInfo(self):
        print(self.piece.colour)
        print(self.piece.name)

    def output(self):
        print("Squre : " + str(self.name) + " " + "Piece : " + str(self.piece) + "\n")