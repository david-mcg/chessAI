class Square:
    name = ""
    piece = 0

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    

    def updateSquare(self, new_piece):
        self.piece = new_piece


    def output(self):
        print("Squre : " + str(self.name) + " " + "Piece : " + str(self.piece) + "\n")