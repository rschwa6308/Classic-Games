#piece class and piece type classes for chess
from Images import *

#print piece_images


class Piece(object):
    def __init__(self,player):
        self.player = player



class Pawn(Piece):
    def __init__(self,player):
        Piece.__init__(self,player)
        self.image = piece_images[["black","white"][player-1] + "_pawn"]


class Rook(Piece):
    def __init__(self,player):
        Piece.__init__(self,player)
        self.image = piece_images[["black","white"][player-1] + "_rook"]


class Knight(Piece):
    def __init__(self,player):
        Piece.__init__(self,player)
        self.image = piece_images[["black","white"][player-1] + "_knight"]


class Bishop(Piece):
    def __init__(self,player):
        Piece.__init__(self,player)
        self.image = piece_images[["black","white"][player-1] + "_bishop"]


class Queen(Piece):
    def __init__(self,player):
        Piece.__init__(self,player)
        self.image = piece_images[["black","white"][player-1] + "_queen"]


class King(Piece):
    def __init__(self,player):
        Piece.__init__(self,player)
        self.image = piece_images[["black","white"][player-1] + "_king"]
