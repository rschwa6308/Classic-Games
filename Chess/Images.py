#load all piece images

from Game_variables import *

import pygame,os
pygame.init()

assets = os.path.join(os.path.join(os.path.split(os.path.abspath(__file__))[0],"Assets"),"pieces")

#black pieces
black_pawn = pygame.image.load(os.path.join(assets,"black_pawn.png"))
black_rook = pygame.image.load(os.path.join(assets,"black_rook.png"))
black_knight = pygame.image.load(os.path.join(assets,"black_knight.png"))
black_bishop = pygame.image.load(os.path.join(assets,"black_bishop.png"))
black_queen = pygame.image.load(os.path.join(assets,"black_queen.png"))
black_king = pygame.image.load(os.path.join(assets,"black_king.png"))

#white pieces
white_pawn = pygame.image.load(os.path.join(assets,"white_pawn.png"))
white_rook = pygame.image.load(os.path.join(assets,"white_rook.png"))
white_knight = pygame.image.load(os.path.join(assets,"white_knight.png"))
white_bishop = pygame.image.load(os.path.join(assets,"white_bishop.png"))
white_queen = pygame.image.load(os.path.join(assets,"white_queen.png"))
white_king = pygame.image.load(os.path.join(assets,"white_king.png"))


pw = int(0.8*bw)
ph = int(0.8*bh)

piece_images = {
    'black_pawn': pygame.transform.scale(black_pawn,(pw,ph)),
    'black_rook': pygame.transform.scale(black_rook,(pw,ph)),
    'black_knight': pygame.transform.scale(black_knight,(pw,ph)),
    'black_bishop': pygame.transform.scale(black_bishop,(pw,ph)),
    'black_queen': pygame.transform.scale(black_queen,(pw,ph)),
    'black_king': pygame.transform.scale(black_king,(pw,ph)),
    
    'white_pawn': pygame.transform.scale(white_pawn,(pw,ph)),
    'white_rook': pygame.transform.scale(white_rook,(pw,ph)),
    'white_knight': pygame.transform.scale(white_knight,(pw,ph)),
    'white_bishop': pygame.transform.scale(white_bishop,(pw,ph)),
    'white_queen': pygame.transform.scale(white_queen,(pw,ph)),
    'white_king': pygame.transform.scale(white_king,(pw,ph))
}
