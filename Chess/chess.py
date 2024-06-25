import pygame as pg

pg.init()

width = 1500
height = 1000
screen = pg.display.set_mode([width, height])
pg.display.set_caption("Play Chess")
font = pg.font.Font("freesansbold.ttf", 20)
big_font = pg.font.Font("freesansbold.ttf", 50)
timer = pg.time.Clock()
fps = 60
blocks = 8 ** 2


white_pieces = [
    'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_loc = [
    (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

black_pieces = [
    'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_loc = [ 
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

captured_white = []
captured_black = []

turn_select = 0
selection = 100
valid_moves = []


#MAKE SURE TO PORT TO A NEW FILE FOR ALL THE IMGS AND PIECE LISTS

#NEED TO SET image.load() LOCATION TO PERSONAL FOLDER LOCATION
bP = pg.transform.scale(pg.image.load('Minigames/Chess/images/bP.png'), (80, 80))
#bP_small = pg.transform.scale(pg.image.load('images/bP.png'), (45, 45))
bR = pg.transform.scale(pg.image.load('Minigames/Chess/images/bR.png'), (80, 80))
#bR_small = pg.transform.scale(pg.image.load('images/bR.png'), (45, 45))
bN = pg.transform.scale(pg.image.load('Minigames/Chess/images/bN.png'), (80, 80))
#bN_small = pg.transform.scale(pg.image.load('images/bN.png'), (45, 45))
bB = pg.transform.scale(pg.image.load('Minigames/Chess/images/bB.png'), (80, 80))
#bB_small = pg.transform.scale(pg.image.load('images/bB.png'), (45, 45))
bQ = pg.transform.scale(pg.image.load('Minigames/Chess/images/bQ.png'), (80, 80))
#bQ_small = pg.transform.scale(pg.image.load('images/bQ.png'), (45, 45))
bK = pg.transform.scale(pg.image.load('Minigames/Chess/images/bK.png'), (80, 80))
#bK_small = pg.transform.scale(pg.image.load('images/bK.png'), (45, 45))

wP = pg.transform.scale(pg.image.load('Minigames/Chess/images/wP.png'), (80, 80))
#wP_small = pg.transform.scale(pg.image.load('images/wP.png'), (45, 45))
wR = pg.transform.scale(pg.image.load('Minigames/Chess/images/wR.png'), (80, 80))
#wR_small = pg.transform.scale(pg.image.load('images/wR.png'), (45, 45))
wN = pg.transform.scale(pg.image.load('Minigames/Chess/images/wN.png'), (80, 80))
#wN_small = pg.transform.scale(pg.image.load('images/wN.png'), (45, 45))
wB = pg.transform.scale(pg.image.load('Minigames/Chess/images/wB.png'), (80, 80))
#wB_small = pg.transform.scale(pg.image.load('images/wB.png'), (45, 45))
wQ = pg.transform.scale(pg.image.load('Minigames/Chess/images/wQ.png'), (80, 80))
#wQ_small = pg.transform.scale(pg.image.load('images/wQ.png'), (45, 45))
wK = pg.transform.scale(pg.image.load('Minigames/Chess/images/wK.png'), (80, 80))
#wK_small = pg.transform.scale(pg.image.load('images/wK.png'), (45, 45))

white_img = [wP, wQ, wK, wN, wR, wB]
#white_img_small = [wP_small, wQ_small, wK_small, wN_small, wR_small, wB_small]
black_img = [bP, bQ, bK, bN, bR, bB]
#white_img_small = [bP_small, bQ_small, bK_small, bN_small, bR_small, bB_small]


piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']



def Draw_Board():
    for i in range(blocks // 2):
        column = i % 4
        row = i // 4

        if row % 2 == 0:
            pg.draw.rect(screen, 'cadetblue', [900 - (column * 200), (row * 100) + 15, 100, 100])
        else:
            pg.draw.rect(screen, 'cadetblue', [1000 - (column * 200), (row * 100) + 15, 100, 100])

        if (row + 1) % 2 == 0:
            pg.draw.rect(screen, 'silver', [900 - (column * 200), (row * 100) + 15, 100, 100])
        else:
            pg.draw.rect(screen, 'silver', [1000 - (column * 200), (row * 100) + 15, 100, 100])

        pg.draw.rect(screen, 'paleturquoise3', [300, 830, 800, 150])
        pg.draw.rect(screen, 'black', [300, 830, 800, 150], 5)
        pg.draw.rect(screen, 'burlywood4', [1150, 50, 300, 900])
        pg.draw.rect(screen, 'black', [1150, 50, 300, 900], 5)

        status = [
            'White: Select Piece to Move', 'White: Select Destination'
            'Black: Select Piece to Move', 'Black: Select Destination']
        screen.blit(big_font.render(status[turn_select], True, 'darkgreen'), (350, 880))

        for i in range(9):
            #(screen, color, tuple(start(x,y),end(x,y)), thickness)
            pg.draw.line(screen, 'black', (300, (100 * i + 15)), (1100, (100 * i + 15)), 1)
            pg.draw.line(screen, 'black', ((100 * i + 300), 15), ((100 * i + 300), 815), 1)



def Draw_Pieces():
    for i in range(len(white_pieces)):
        piece_index = piece_list.index(white_pieces[i])
        screen.blit(white_img[piece_index], (white_loc[i][0] * 100 + 310, white_loc[i][1] * 100 + 25))
        #useful for if different sized images
        #if white_pieces[i] == 'pawn':
        #    screen.blit(wP, (white_loc[i][0] * 100 + 22, white_loc[i][1] * 100 + 30))
        #else:
        #    screen.blit(white_img[piece_index], (white_loc[i][0] * 100 + 22, white_loc[i][1] * 100 + 30))
    
        if turn_select < 2:
            if selection == i:
                pg.draw.rect(screen, 'red', [white_loc[i][0] * 100 + 300, white_loc[i][1] * 100 + 16, 99, 99], 1)

    for i in range(len(black_pieces)):
        piece_index = piece_list.index(black_pieces[i])
        #source.blit(image/source of drawing, destination (x, y)) || I changed the relative positions by using the +num values
        screen.blit(black_img[piece_index], (black_loc[i][0] * 100 + 310, black_loc[i][1] * 100 + 25))

        if turn_select >= 2:
            if selection == i:
                pg.draw.rect(screen, 'red', [black_loc[i][0] * 100 + 301, black_loc[i][1] * 100 + 16, 99, 99], 2)



def check_ops():
    pass



running = True
while running:
    timer.tick(fps)
    screen.fill("darkgreen")

    Draw_Board()
    Draw_Pieces()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x_coor = event.pos[0] // 100 - 3
            y_coor = event.pos[1] // 100
            clk_coor = (x_coor, y_coor)

            #For White
            if turn_select < 2:
                if clk_coor in white_loc:
                    selection = white_loc.index(clk_coor)
                    if turn_select == 0:
                        turn_select = 1
                if clk_coor in valid_moves and selection != 100:
                    white_loc[selection] = clk_coor
                    if clk_coor in black_loc:
                        black_piece = black_loc.index(clk_coor)
                        captured_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_loc.pop(black_piece)
                    
                    black_ops = check_ops(black_pieces, black_loc, 'black')
                    white_ops = check_ops(white_pieces, white_loc, 'white')
                    turn_select = 2
                    selection = 100
                    valid_moves = []
            
            #For Black
            if turn_select >= 2:
                if clk_coor in black_loc:
                    selection = black_loc.index(clk_coor)
                    if turn_select == 2:
                        turn_select = 3
                if clk_coor in valid_moves and selection != 100:
                    black_loc[selection] = clk_coor
                    if clk_coor in white_loc:
                        white_piece = white_loc.index(clk_coor)
                        captured_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_loc.pop(white_piece)
                    
                    white_ops = check_ops(white_pieces, white_loc, 'white')
                    black_ops = check_ops(black_pieces, black_loc, 'black')
                    turn_select = 0
                    selection = 100
                    valid_moves = []

    pg.display.flip()
pg.quit()
