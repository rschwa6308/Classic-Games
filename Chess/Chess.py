#chess game

#import modules
from random import *
from time import *
import pygame,sys,os
from pygame import *
from pygame.locals import *

#import game elements
from Pieces import *
from Colors import *
from Images import *
from Is_Move import *




#display function
def display(screen,board):
    #draw background
    for y in range(8):
        if y%2 == 0:
            for x in range(8):
                if x%2 == 0:
                    pygame.draw.rect(screen,light_tan,Rect(x*bw,y*bh,bw,bh),0)
                else:
                    pygame.draw.rect(screen,dark_tan,Rect(x*bw,y*bh,bw,bh),0)
        else:
            for x in range(8):
                if x%2 == 0:
                    pygame.draw.rect(screen,dark_tan,Rect(x*bw,y*bh,bw,bh),0)
                else:
                    pygame.draw.rect(screen,light_tan,Rect(x*bw,y*bh,bw,bh),0)
    #draw pieces
    for y in range(len(board)):
        for x in range(len(board[y])):
            if isinstance(board[y][x],Piece):
                screen.blit(board[y][x].image,(x*bw+int((bw-0.8*bw)/2),y*bh+int((bh-0.8*bh)/2)))
    #flip display
    pygame.display.update()





#funcion to put yellow box around selected piece (highligh function)
def highlight(screen,board,pos):
    display(screen,board)
    pygame.draw.rect(screen,yellow,Rect(pos[0]*bw,pos[1]*bh,bw,bh),3)
    pygame.display.update()



#function to move a piece on a specified board
def move(board,start,end):
    board[end[1]][end[0]] = board[start[1]][start[0]]
    board[start[1]][start[0]] = 0



#function to change turn and display board
def change_turn(screen,board,turn):
    turn = 3-turn
    pygame.display.set_caption("Player " + str(turn) + "\'s turn")
    display(screen,board)
    return turn




#main function
def main():
    #center screen
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    #init pygame
    pygame.init()

    #set up screen
    screen = pygame.display.set_mode((s_width,s_height))

    #set up caption
    pygame.display.set_caption("Player 1's turn")


    #init board (0 => empty cell)
    board = [[Rook(1),Knight(1),Bishop(1),King(1),Queen(1),Bishop(1),Knight(1),Rook(1)],
             [Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1)],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [Pawn(2),Pawn(2),Pawn(2),Pawn(2),Pawn(2),Pawn(2),Pawn(2),Pawn(2)],
             [Rook(2),Knight(2),Bishop(2),Queen(2),King(2),Bishop(2),Knight(2),Rook(2)]]


    display(screen,board)


    selected = (-1,-1)
    global turn
    turn = 1
    #game loop
    done = False
    clock = pygame.time.Clock()
    while not done:
        clock.tick
        #user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN: 
                if event.button == 1:
                    z = pygame.mouse.get_pos()
                    x = z[0]/bw
                    y = z[1]/bw
                    #select piece
                    if selected == (-1,-1) and board[y][x] != 0:
                        if board[y][x].player == turn:
                            highlight(screen,board,(x,y))
                            selected = (x,y)
                    #select target
                    elif selected != (-1,-1):
                        check_move = True
                        if isinstance(board[y][x], Piece):
                            if board[y][x].player == turn:
                                print "switch selected"
                                display(screen, board)
                                selected = (x,y)
                                highlight(screen,board,selected)
                                check_move = False
                        if check_move:
                            if is_move(board,board[selected[1]][selected[0]],selected,(x,y)):
                                board[y][x] = board[selected[1]][selected[0]]
                                board[selected[1]][selected[0]] = 0
                                display(screen, board)
                                turn = 3-turn
                                selected = (-1,-1)

        




main()










