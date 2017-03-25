#requires pygame module to run
import math
from random import *
from funcs import *
from HALOS import *
from ZALOS import *




#initiate pygame
pygame.init()


#initialize caption
pygame.display.set_caption("player " + str(turn) + "'s turn")

#display board
display(board)


#game loop
global done
done = False
while not done:
    
    #user input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
            sys.exit()
        #HALOS stuff
        elif event.type == KEYDOWN:
            if event.key == K_h:
                move = HALOS(board,kings,turn)
            elif event.key == K_z:
                move = ZALOS(board,kings,turn)
            if event.key == K_h or event.key == K_z:
                board[move.start[1]][move.start[0]] = 0
                board[move.end[1]][move.end[0]] = turn
                for cap in move.captured:
                    board[cap[1]][cap[0]] = 0
                    try: kings.remove(cap)
                    except: pass
                if is_win(board,turn):
                    print "Player " + str(turn) + " wins!"
                    display(board)
                    sleep(2)
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                #check if piece is king and then alter king list
                if (move.start[0],move.start[1]) in kings:
                    kings.remove((move.start[0],move.start[1]))
                    kings.append((move.end[0],move.end[1]))
                #ckeck for king-me's
                if move.end[1] == -7*(turn-2) and not (move.end[0],move.end[1]) in kings:
                    kings.append(move.end)
                turn = change_turn(turn)
                pygame.display.set_caption("player " + str(turn) + "'s turn")
                display(board)

                
        elif event.type == MOUSEBUTTONDOWN:
            #select piece
            if event.button == 1:
                z = pygame.mouse.get_pos()
                z = [z[0]/bw,z[1]/bh]
                
                #if clicked is turn's piece
                if board[z[1]][z[0]] == turn:
                    highlight(z)
                    selected = z
                    
                #if clicked is target square
                if selected != z and selected != (-1,-1) and z[0]%2 != z[1]%2:
                    #print "clicking target"
                    if is_move(selected,z,turn,kings):
                        #move piece
                        #print "moving piece"
                        board[selected[1]][selected[0]] = 0
                        board[z[1]][z[0]] = turn
                        #check if piece is king and then alter king list
                        if (selected[0],selected[1]) in kings:
                            kings.remove((selected[0],selected[1]))
                            kings.append((z[0],z[1]))
                        #ckeck for king-me's
                        if z[1] == -7*(turn-2):
                            kings.append(z)
                        if is_win(board,turn):
                            print "Player " + str(turn) + " wins!"
                            display(board)
                            sleep(2)
                            pygame.display.quit()
                            pygame.quit()
                            quit()
                        turn = change_turn(turn)
                        pygame.display.set_caption("player " + str(turn) + "'s turn")
                        display(board)
                        
    



















