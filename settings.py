
#######WINDOW##########
HEIGHT = 775
WIDTH = 775
#######COLOURS##########
WHITE = (255,255,255)
BLACK = (0,0,0)

#######BOARDS###########
#returns a list of 0's for x in range of 9
testBoard = [[0 for x in range(9)] for x in range(9)]

#######POSITIONS AND SIZES######
#position that the grid starts at, x, and y coordinates
gridPos = (75,100)
#the size of a box
cellSize = 25
#the size of the grid, basically the number of cells * the cell size
gridSize = cellSize*25

position1 = [(11, 7), (11, 6), (12, 6), (12, 7), (13, 8), (13, 9), (14, 9), (14, 8), (11, 14), (12, 14), (13, 14), (12, 15), (11, 15), (10, 15), (3, 8), (3, 9), (3, 10), (20, 18), (20, 19), (20, 20), (4, 20), (5, 20), (6, 20), (20, 9), (21, 9), (22, 9)]
position2 = [(7, 5), (8, 5), (9, 5), (13, 5), (14, 5), (15, 5), (12, 7), (12, 8), (12, 9), (10, 7), (10, 8), (10, 9), (9, 10), (8, 10), (7, 10), (13, 10), (14, 10), (15, 10), (17, 9), (17, 8), (17, 7), (5, 9), (5, 8), (5, 7), (13, 12), (14, 12), (15, 12), (9, 12), (8, 12), (7, 12), (10, 13), (10, 14), (10, 15), (12, 13), (12, 14), (12, 15), (13, 17), (14, 17), (15, 17), (9, 17), (8, 17), (7, 17), (5, 15), (5, 14), (5, 13), (17, 13), (17, 14), (17, 15)]

position3 = [(10, 6), (11, 6), (12, 6), (11, 7), (11, 8), (10, 9), (11, 9), (12, 9), (10, 11), (11, 11), (12, 11), (10, 12), (11, 12), (12, 12), (12, 14), (11, 14), (10, 14), (11, 15), (11, 16), (11, 17), (10, 17), (12, 17)]
#########CUSTOM EVENTS FOR TIMER##########




######TIMER#######