#function to detirmine if it is a move
from Pieces import *


#player 1 starts at top and moves down
#player 2 starts at bottom and moves up


def get_between_hor(sPos, ePos):
    sx = sPos[0]
    sy = sPos[1]
    ex = ePos[0]
    ey = ePos[1]

    if sx == ex:
        if sy > ey:     #move up screen
            return [(sx,y) for y in range(ey,sy-1)]
        else:           #move down screen
            return [(sx,y) for y in range(sy+1,ey)]
    elif sy == ey:
        if sx > ex:     #move left screen
            return [(x,sy) for x in range(ex,sx-1)]
        else:           #move right screen
            return [(x,sy) for x in range(sx+1,ex)]



def get_between_diag(sPos, ePos):
    sx = sPos[0]
    sy = sPos[1]
    ex = ePos[0]
    ey = ePos[1]

    if sy > ey:     #move up screen
        if sx > ex:     #move up-left screen
            return [(sx-step,sy-step) for step in range(1,sy-ey)]
        else:           #move up-right screen
            return [(sx+step,sy-step) for step in range(1,sy-ey)]
    else:           #move down screen
        if sx > ex:     #move down-left screen
            return [(sx-step,sy+step) for step in range(1,ey-sy)]
        else:           #move down-right screen
            print "plz"
            return [(sx+step,sy+step) for step in range(1,ey-sy)]

        


  
def is_move(board,piece,start,end):
    #return True
    me = piece.player
    you = 3-me
    sx = start[0]
    sy = start[1]
    ex = end[0]
    ey = end[1]
    cap = False

    if isinstance(board[ey][ex], Piece):
        if board[ey][ex].player is you:
            cap = True



    #pawn
    if me == 1:                     #player 1
        if isinstance(piece,Pawn):
            print "pawn"
            if sx == ex and board[ey][ex] == 0:
                print "same x"
                if sy-ey == -1:
                    return True
                elif sy-ey == -2:
                    if sy == 1:
                        return True
            if abs(sx-ex) == 1 and isinstance(board[ey][ex],Piece):
                if sy-ey == -1 and board[ey][ex].player == you:
                    return True
    else:                           #player 2
        if isinstance(piece,Pawn):
            print "pawn"
            if sx == ex and board[ey][ex] == 0:
                print "same x"
                if sy-ey == 1:
                    return True
                elif sy-ey == 2:
                    if sy == 6:
                        return True
            if abs(sx-ex) == 1 and isinstance(board[ey][ex],Piece):
                if sy-ey == 1 and board[ey][ex].player == you:
                    return True    

    #rook
    if isinstance(piece, Rook):
        print "rook"
        if sx != ex and sy != ey:
            "diagonal attempt"
            return False
        
        checks = get_between_hor((sx,sy),(ex,ey))
        for c in checks:
            if board[c[1]][c[0]] != 0:
                return False
        if cap:
            return True
        else:
            if board[ey][ex] is 0:
                return True
        return False

    #bishop
    if isinstance(piece, Bishop):
        if abs(sx - ex) != abs(sy - ey):
            print "non-45* attempt"
            return False
        
        checks = get_between_diag((sx,sy),(ex,ey))
        for c in checks:
            if board[c[1]][c[0]] != 0:
                return False
        if cap:
            return True
        else:
            if board[ey][ex] is 0:
                return True
        return False


    #queen
    if isinstance(piece, Queen):
        #hor checks
        if sx == ex or sy == ey:
            print "hor queen"
            checks = get_between_hor((sx,sy),(ex,ey))
            for c in checks:
                if board[c[1]][c[0]] != 0:
                    return False
        #diag checks
        print ""
        print sx-ex
        print sy-ey
        if abs(sx - ex) == abs(sy - ey):
            print "diag queen"
            checks = get_between_diag((sx,sy),(ex,ey))
            for c in checks:
                if board[c[1]][c[0]] != 0:
                    return False
        else:
            return False
        
        if cap:
            return True
        else:
            if board[ey][ex] is 0:
                return True
        return False



   
                    
    return False

















