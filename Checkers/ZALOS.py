#ZALOS (HALOS competetor)

#ai to play checkers

from random import *
from time import *

#ZALOS takes an 8x8 board (2d array) and her piece# and returns a tuple her move's start and end location's coords as tuples ((x1,y1),(x2,y2))



#move values schema

#bonus per capture = +1
a = 1

#trans out of own back row penalty = -2
d = -2

#king-me bonus = +3
e = 3
#capture of enemy king bonus = +3
f = 3




#define main
def ZALOS(board,kings,me):
    #get all moves
    moves = get_moves(board,kings,me)

    #assign values to all moves
    for move in moves:
        
        #num of caps
        move.value = len(move.captured)
        
        #special bonuses/penalties
        if move.start[1] == 7*(me-1):       #out of back row
            move.value += d
        if move.end[1] == -7*(me-2):      #into enemy back row (far row)
            move.value += e
        for cap in move.captured:
            if cap in kings:
                move.value += 3

    #find and return random most valuable move
    most = -10000
    best = []
    for move in moves:
        if move.value > most:
            best = [move]
            most = move.value
        elif move.value == most:
            best.append(move)
    out = best[randint(0,len(best)-1)]
    print "value: " + str(out.value)
    return out




#define Move class (can have type "trans", "single", or "double")
class Move():
    def __init__(self,start,end,captured):
        self.start = start
        self.end = end
        self.captured = captured




#define function to get list of all piece coords(x,y) for a certain player('me')
def get_pieces(board,me):
    pieces = []
    for y in range(8):
        for x in range(8):
            p = board[y][x]
            if p != me:
                pass
            elif p == me:
                pieces.append((x,y))
    return pieces





#define function to get all possible moves of 'me'
def get_moves(board,kings,me):
    #init moves list
    moves = []
    
    #get pieces of me
    pieces = get_pieces(board,me)

    for p in pieces:

        #print p
        x = p[0]
        y = p[1]

        #king
        if p in kings:
            #trans
            #up
            if  7 >= y-1 >= 0 and 7 >= x-1 >= 0:                     #left
                    if board[y-1][x-1] == 0:
                        moves.append(Move(p,(x-1,y-1),[]))
            if 7 >= y-1 >= 0 and 7 >= x+1 >= 0:                      #right
                if board[y-1][x+1] == 0:
                    moves.append(Move(p,(x+1,y-1),[]))
            #down
            if  7 >= y+1 >= 0 and 7 >= x-1 >= 0:                     #left
                    if board[y+1][x-1] == 0:
                        moves.append(Move(p,(x-1,y+1),[]))
            if 7 >= y+1 >= 0 and 7 >= x+1 >= 0:                      #right
                if board[y+1][x+1] == 0:
                    moves.append(Move(p,(x+1,y+1),[]))
            #ADD JUMPING FUNCTIONALITY HERE
            ####
                    ####
                            ####
    

        #p1
        elif me == 1:
            #trans
            if  7 >= y+1 >= 0 and 7 >= x-1 >= 0:                     #left
                if board[y+1][x-1] == 0:
                    moves.append(Move(p,(x-1,y+1),[]))
            if 7 >= y+1 >= 0 and 7 >= x+1 >= 0:                      #right
                if board[y+1][x+1] == 0:
                    moves.append(Move(p,(x+1,y+1),[]))
                    
            #single
            if 7 >= y+2 >= 0 and 7 >= x-2 >= 0:                      #left
                if board[y+1][x-1] == 2 and board[y+2][x-2] == 0:
                    moves.append(Move(p,(x-2,y+2),[(x-1,y+1)]))
            if 7 >= y+2 >= 0 and 7 >= x+2 >= 0:                      #right
                if board[y+1][x+1] == 2 and board[y+2][x+2] == 0:
                    moves.append(Move(p,(x+2,y+2),[(x+1,y+1)]))
        

        
        #p2
        elif me == 2:
            #print p
            x = p[0]
            y = p[1]
            
            #trans
            if 7 >= y-1 >= 0 and 7 >= x-1 >= 0:                      #left
                if board[y-1][x-1] == 0:
                    moves.append(Move(p,(x-1,y-1),[]))
            if 7 >= y-1 >= 0 and 7 >= x+1 >= 0:                      #right
                if board[y-1][x+1] == 0:                            
                    moves.append(Move(p,(x+1,y-1),[]))

            #single
            if 7 >= y-2 >= 0 and 7 >= x-2 >= 0:                      #left
                if board[y-1][x-1] == 1 and board[y-2][x-2] == 0:
                    moves.append(Move(p,(x-2,y-2),[(x-1,y-1)]))
            if 7 >= y-2 >= 0 and 7 >= x+2 >= 0:                      #right
                if board[y-1][x+1] == 1 and board[y-2][x+2] == 0:
                    moves.append(Move(p,(x+2,y-2),[(x+1,y-1)]))


    #return moves list
    return moves











#test code
##board = [[0,1,0,1,0,1,0,1],
##         [1,0,1,0,1,0,1,0],
##         [0,1,0,1,0,1,0,1],
##         [0,0,0,0,0,0,0,0],
##         [0,0,0,0,0,0,0,0],
##         [2,0,2,0,2,0,2,0],
##         [0,2,0,2,0,2,0,2],
##         [2,0,2,0,2,0,2,0]]



##for move in get_moves(board,2):
##    print "kind: " + str(move.kind) + ", start: " + str(move.start) + ", end: " + str(move.end)


##out = HALOS(board,1)
##print "kind: " + str(out.kind) + ", start: " + str(out.start) + ", end: " + str(out.end)


##def display(board):
##    for row in board:
##        z = ""
##        for col in row:
##            if col == 0:
##                z = z + ". "
##            elif col == 1:
##                z = z + "X "
##            elif col == 2:
##                z = z + "O "
##        print z
##
###test game
##for i in range(100):
##    if i%2 == 0:
##        me = 1
##    else:
##        me = 2
##    
##    print "\n\n"
##    move = HALOS(board,me)
##    #print "kind: " + str(move.kind) + ", start: " + str(move.start) + ", end: " + str(move.end)
##    board[move.start[1]][move.start[0]] = 0
##    board[move.end[1]][move.end[0]] = me
##    for cap in move.captured:
##        board[cap[1]][cap[0]] = 0
##
##    sleep(0.5)
##    display(board)




         
