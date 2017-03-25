#game variables


#init board
global board
board = [[0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [2,0,2,0,2,0,2,0],
         [0,2,0,2,0,2,0,2],
         [2,0,2,0,2,0,2,0]]

##board = [[0,1,0,1,0,1,0,1],
##         [1,0,0,0,1,0,1,0],
##         [0,1,0,1,0,1,0,1],
##         [0,0,2,0,0,0,2,0],
##         [0,0,0,0,0,1,0,0],
##         [0,0,2,0,2,0,2,0],
##         [0,0,0,0,0,0,0,0],
##         [0,0,0,0,0,0,0,0]]

#init kings list
global kings
kings = []
#kings = [(1,2),(2,5)]

#initiate turn variable
global turn
turn = 1

#initiate selected variable
global selected
selected = (-1,-1)

