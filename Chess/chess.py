import pygame as pg
#from variables import *
#could use this instead and port all of the variables over

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
select_piece = ''


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

white_moved = [
    False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False]
black_moved = [
    False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False]

captured_white = []
captured_black = []

white_eP = (100,100)
black_eP = (100,100)

white_promote = False
black_promote = False

promote_index = 100

easy_castle = False

turn_select = 0
counter = 0
selection = 100
valid_moves = []

winner = ''

check = False
checkmate = False
stalemate = False
end_game = False

promotion_list = white_pieces[:4]


#MAKE SURE TO PORT TO A NEW FILE FOR ALL THE IMGS AND PIECE LISTS

#NEED TO SET image.load() LOCATION TO PERSONAL FOLDER LOCATION
bP = pg.transform.scale(pg.image.load('Games/Chess/images/bP.png'), (80, 80))
#bP_small = pg.transform.scale(pg.image.load('images/bP.png'), (45, 45))
bR = pg.transform.scale(pg.image.load('Games/Chess/images/bR.png'), (80, 80))
#bR_small = pg.transform.scale(pg.image.load('images/bR.png'), (45, 45))
bN = pg.transform.scale(pg.image.load('Games/Chess/images/bN.png'), (80, 80))
#bN_small = pg.transform.scale(pg.image.load('images/bN.png'), (45, 45))
bB = pg.transform.scale(pg.image.load('Games/Chess/images/bB.png'), (80, 80))
#bB_small = pg.transform.scale(pg.image.load('images/bB.png'), (45, 45))
bQ = pg.transform.scale(pg.image.load('Games/Chess/images/bQ.png'), (80, 80))
#bQ_small = pg.transform.scale(pg.image.load('images/bQ.png'), (45, 45))
bK = pg.transform.scale(pg.image.load('Games/Chess/images/bK.png'), (80, 80))
#bK_small = pg.transform.scale(pg.image.load('images/bK.png'), (45, 45))

wP = pg.transform.scale(pg.image.load('Games/Chess/images/wP.png'), (80, 80))
#wP_small = pg.transform.scale(pg.image.load('images/wP.png'), (45, 45))
wR = pg.transform.scale(pg.image.load('Games/Chess/images/wR.png'), (80, 80))
#wR_small = pg.transform.scale(pg.image.load('images/wR.png'), (45, 45))
wN = pg.transform.scale(pg.image.load('Games/Chess/images/wN.png'), (80, 80))
#wN_small = pg.transform.scale(pg.image.load('images/wN.png'), (45, 45))
wB = pg.transform.scale(pg.image.load('Games/Chess/images/wB.png'), (80, 80))
#wB_small = pg.transform.scale(pg.image.load('images/wB.png'), (45, 45))
wQ = pg.transform.scale(pg.image.load('Games/Chess/images/wQ.png'), (80, 80))
#wQ_small = pg.transform.scale(pg.image.load('images/wQ.png'), (45, 45))
wK = pg.transform.scale(pg.image.load('Games/Chess/images/wK.png'), (80, 80))
#wK_small = pg.transform.scale(pg.image.load('images/wK.png'), (45, 45))

white_img = [wP, wQ, wK, wN, wR, wB]
#white_img_small = [wP_small, wQ_small, wK_small, wN_small, wR_small, wB_small]
black_img = [bP, bQ, bK, bN, bR, bB]
#white_img_small = [bP_small, bQ_small, bK_small, bN_small, bR_small, bB_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

status = [
    'White: Select Piece to Move', 'White: Select Destination',
    'Black: Select Piece to Move', 'Black: Select Destination']



def Draw_Board(status):
    for i in range(blocks // 2):
        column = i % 4
        row = i // 4

        if row % 2 == 0:
            pg.draw.rect(screen, 'silver', [900 - (column * 200), (row * 100) + 15, 100, 100])
        else:
            pg.draw.rect(screen, 'silver', [1000 - (column * 200), (row * 100) + 15, 100, 100])

        if (row + 1) % 2 == 0:
            pg.draw.rect(screen, 'cadetblue', [900 - (column * 200), (row * 100) + 15, 100, 100])
        else:
            pg.draw.rect(screen, 'cadetblue', [1000 - (column * 200), (row * 100) + 15, 100, 100])

        pg.draw.rect(screen, 'paleturquoise3', [300, 830, 800, 150])
        pg.draw.rect(screen, 'black', [300, 830, 800, 150], 5)
        pg.draw.rect(screen, 'burlywood4', [1150, 15, 300, 975])
        pg.draw.rect(screen, 'black', [1150, 15, 300, 975], 5)

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
                pg.draw.rect(screen, 'red', [white_loc[i][0] * 100 + 301, white_loc[i][1] * 100 + 16, 99, 99], 1)

    for i in range(len(black_pieces)):
        piece_index = piece_list.index(black_pieces[i])
        #source.blit(image/source of drawing, destination (x, y)) || I changed the relative positions by using the +num values
        screen.blit(black_img[piece_index], (black_loc[i][0] * 100 + 310, black_loc[i][1] * 100 + 25))

        if turn_select >= 2:
            if selection == i:
                pg.draw.rect(screen, 'red', [black_loc[i][0] * 100 + 301, black_loc[i][1] * 100 + 16, 99, 99], 1)

def Draw_Captured():
    for i in range(len(captured_black)):
        captured_piece = captured_black[i]
        piece_index = piece_list.index(captured_piece)
        screen.blit(white_img[piece_index], (1150, 65 * i + 15))

    for i in range(len(captured_white)):
        captured_piece = captured_white[i]
        piece_index = piece_list.index(captured_piece)
        screen.blit(black_img[piece_index], (1350, 65 * i + 15))
        #Maybe try and use an if index len < num switch the screen.blit dimensions



def Pawn(position, color):
    move_list = []

    if color == 'black':
        if (position[0], position[1] + 1) not in black_loc and \
        (position[0], position[1] + 1) not in white_loc and \
        position[1] < 7:
            move_list.append((position[0], position[1] + 1))

            if (position[0], position[1] + 2) not in black_loc and \
            (position[0], position[1] + 2) not in white_loc and \
            position[1] == 1:
                move_list.append((position[0], position[1] + 2))

        if (position[0] + 1, position[1] + 1) in white_loc:
            move_list.append((position[0] + 1, position[1] + 1))

        if (position[0] - 1, position[1] + 1) in white_loc:
            move_list.append((position[0] - 1, position[1] + 1))

        #en Passant Checks
        #if (position[0] + 1, position[1] + 1) == white_eP:
        #    move_list.append((position[0] + 1, position[1] + 1))

        #if (position[0] - 1, position[1] + 1) == white_eP:
        #    move_list.append((position[0] - 1, position[1] + 1))


    elif color == 'white':
        if (position[0], position[1] - 1) not in white_loc and \
        (position[0], position[1] - 1) not in black_loc and \
        position[1] > 0:
            move_list.append((position[0], position[1] - 1))

            if (position[0], position[1] - 2) not in white_loc and \
            (position[0], position[1] - 2) not in black_loc and \
            position[1] == 6:
                move_list.append((position[0], position[1] - 2))

        if (position[0] + 1, position[1] - 1) in black_loc:
            move_list.append((position[0] + 1, position[1] - 1))

        if (position[0] - 1, position[1] - 1) in black_loc:
            move_list.append((position[0] - 1, position[1] - 1))

        #en Passant Checks
        #if (position[0] + 1, position[1] - 1) == black_eP:
        #    move_list.append((position[0] + 1, position[1] - 1))

        #if (position[0] - 1, position[1] - 1) == black_eP:
        #    move_list.append((position[0] - 1, position[1] - 1))

    return move_list

def Rook(position, color):
    move_list = []

    if color == 'black':
        allies = black_loc
        opponent = white_loc
    else:
        allies = white_loc
        opponent = black_loc

    for i in range(4):
        path = True
        chain = 1

        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0

        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in allies and \
            0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                move_list.append((position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in opponent:
                    path = False
                chain += 1

            else:
                path = False

    return move_list

def Knight(position, color):
    move_list = []
    targets = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]

    if color == 'black':
        allies = black_loc
    else:
        allies = white_loc

    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in allies and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            move_list.append(target)

    return move_list

def Bishop(position, color):
    move_list = []

    if color == 'black':
        allies = black_loc
        opponent = white_loc
    else:
        allies = white_loc
        opponent = black_loc

    for i in range(4):
        path = True
        chain = 1

        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1

        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in allies and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                move_list.append((position[0] + (chain * x), position[1] + (chain * y)))

                if (position[0] + (chain * x), position[1] + (chain * y)) in opponent:
                    path = False
                chain += 1

            else:
                path = False

    return move_list

def Queen(position, color):
    move_list = Bishop(position, color)
    move_list2 = Rook(position, color)

    for i in range(len(move_list2)):
        move_list.append(move_list2[i])

    return move_list

def King(position, color):
    move_list = []
    targets = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (0,1), (-1,0), (0,-1)]
    castling = Castle()

    if color == 'black':
        allies = black_loc
    else:
        allies = white_loc

    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in allies and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            move_list.append(target)

    return move_list, castling



def check_ops(pieces, locations, turn):
    global castle_moves
    castle_moves = []
    move_list = []
    all_moves = []

    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]

        if piece == 'pawn':
            move_list = Pawn(location, turn)
        elif piece == 'rook':
            move_list = Rook(location, turn)
        elif piece == 'knight':
            move_list = Knight(location, turn)
        elif piece == 'bishop':
            move_list = Bishop(location, turn)
        elif piece == 'queen':
            move_list = Queen(location, turn)
        elif piece == 'king':
            move_list, castle_moves = King(location, turn)

        all_moves.append(move_list)

    return all_moves

def check_valid():
    if turn_select < 2:
        ops_list = white_ops
    elif turn_select >= 2:
        ops_list = black_ops

    valid_ops = ops_list[selection]

    return valid_ops

def draw_moves(moves):
    color = 'cyan'

    for i in range(len(moves)):
        pg.draw.circle(screen, color, (moves[i][0] * 100 + 351, moves[i][1] * 100 + 67), 5)



'''
def turn_end(black_pieces, black_loc, white_pieces, white_loc):
    black_ops = check_ops(black_pieces, black_loc, 'black')
    white_ops = check_ops(white_pieces, white_loc, 'white')
    turn_select = 2
    selection = 100
    valid_moves = []

    return black_ops, white_ops, turn_select, selection, valid_moves
'''


def Check():

    if 'king' in white_pieces and 'king' in black_pieces:
        wK_index = white_pieces.index("king")
        wK_loc = white_loc[wK_index]

        bK_index = black_pieces.index("king")
        bK_loc = black_loc[bK_index]

        for i in range(len(black_ops)):
            if wK_loc in black_ops[i]:
                check = True
                if counter < 25:
                    pg.draw.rect(screen, 'red1', [white_loc[wK_index][0] * 100 + 301, white_loc[wK_index][1] * 100 + 16, 99, 99], 5)

        for i in range(len(white_ops)):
            if bK_loc in white_ops[i]:
                check = True
                if counter < 25:
                    pg.draw.rect(screen, 'red1', [black_loc[bK_index][0] * 100 + 301, black_loc[bK_index][1] * 100 + 16, 99, 99], 5)

    else:
        if 'king' not in white_pieces:
            pass
        
        elif 'king' not in black_pieces:
            pass
        
        else:
            pass



def Promotion():
    pawn_index = []
    white_pro = False
    black_pro = False
    pro_index = 100

    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            pawn_index.append(i)
    
    for i in range(len(pawn_index)):
        if white_loc[pawn_index[i]][1] == 0:
            white_pro = True
            pro_index = pawn_index[i]
    
    pawn_index = []
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            pawn_index.append(i)
    
    for i in range(len(pawn_index)):
        if black_loc[pawn_index[i]][1] == 7:
            black_pro = True
            pro_index = pawn_index[i]

    return white_pro, black_pro, pro_index

def draw_promotion():
    pg.draw.rect(screen, 'silver', [270, 370, 860, 150])
    pg.draw.rect(screen, 'black', [270, 370, 860, 150], 5)

    if white_promote:
        for i in range(len(promotion_list)):
            piece = promotion_list[i]
            index = piece_list.index(piece)
            screen.blit(white_img[index], (345 + 210 * i, 400))

    elif black_promote:
        for i in range(len(promotion_list)):
            piece = promotion_list[i]
            index = piece_list.index(piece)
            screen.blit(black_img[index], (345 + 210 * i, 400))

def promotion_select():
    mouse_pos = pg.mouse.get_pos()
    clk = pg.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100 - 3
    y_pos = (mouse_pos[1] - 15) // 100

    if white_promote and clk and 0 <= x_pos <= 1 and 3 <= y_pos <=4:
        white_pieces[promote_index] = promotion_list[0]
    elif white_promote and clk and 2 <= x_pos <= 3 and 3 <= y_pos <=4:
        white_pieces[promote_index] = promotion_list[1]
    elif white_promote and clk and 4 <= x_pos <= 5 and 3 <= y_pos <=4:
        white_pieces[promote_index] = promotion_list[2]
    elif white_promote and clk and 6 <= x_pos <= 7 and 3 <= y_pos <=4:
        white_pieces[promote_index] = promotion_list[3]
    
    if black_promote and clk and 0 <= x_pos <= 1 and 3 <= y_pos <=4:
        black_pieces[promote_index] = promotion_list[0]
    elif black_promote and clk and 2 <= x_pos <= 3 and 3 <= y_pos <=4:
        black_pieces[promote_index] = promotion_list[1]
    elif black_promote and clk and 4 <= x_pos <= 5 and 3 <= y_pos <=4:
        black_pieces[promote_index] = promotion_list[2]
    elif black_promote and clk and 6 <= x_pos <= 7 and 3 <= y_pos <=4:
        black_pieces[promote_index] = promotion_list[3]



def Castle():
    castle_moves = []
    rook_index = []
    rook_loc = []
    king_index = 0
    king_loc = (0,0)

    if turn_select >= 2:
        for i in range(len(white_pieces)):
            if white_pieces[i] == 'rook':
                rook_index.append(white_moved[i])
                rook_loc.append(white_loc[i])

            if white_pieces[i] == 'king':
                king_index = i
                king_loc = white_loc[i]
            
            print(rook_index)
        
        if not white_moved[king_index] and False in rook_index and not check:
            for i in range(len(rook_index)):
                print(rook_index)
                castle = True
                if rook_loc[i][0] > king_loc[0]:
                    empty_loc = [(king_loc[0] + 1, king_loc[1]), 
                                    (king_loc[0] + 2, king_loc[1]), 
                                    (king_loc[0] + 3, king_loc[1])]
                
                else:
                    empty_loc = [(king_loc[0] - 1, king_loc[1]), 
                                    (king_loc[0] - 2, king_loc[1])]
                
                for j in range(len(empty_loc)):
                    if empty_loc[j] in white_loc or empty_loc[j] in black_loc or empty_loc[j] in black_ops or rook_index[i]:
                        castle = False
                    
                if castle:
                    castle_moves.append((empty_loc[1], empty_loc[0]))

    else:
        for i in range(len(black_pieces)):
            if black_pieces[i] == 'rook':
                rook_index.append(black_moved[i])
                rook_loc.append(black_loc[i])

            if black_pieces[i] == 'king':
                king_index = i
                king_loc = black_loc[i]
        
        if not black_moved[king_index] and False in rook_index and not check:
            for i in range(len(rook_index)):
                castle = True
                if rook_loc[i][0] > king_loc[0]:
                    empty_loc = [(king_loc[0] + 1, king_loc[1]), 
                                    (king_loc[0] + 2, king_loc[1]), 
                                    (king_loc[0] + 3, king_loc[1])]
                
                else:
                    empty_loc = [(king_loc[0] - 1, king_loc[1]), 
                                    (king_loc[0] - 2, king_loc[1])]
                
                for j in range(len(empty_loc)):
                    if empty_loc[j] in white_loc or empty_loc[j] in black_loc or empty_loc[j] in white_ops or rook_index[i]:
                        castle = False
                    
                if castle:
                    castle_moves.append((empty_loc[1], empty_loc[0]))
    
    return castle_moves

def draw_castle(moves):
    color = 'cyan'

    for i in range(len(moves)):
        pg.draw.circle(screen, color, (moves[i][0][0] * 100 + 351, moves[i][0][1] * 100 + 67), 5)
        #screen.blit(font.render('king', True, 'black), (moves[i][0][0] * 100 + 351, moves[i][0][1] * 100 + 67))
        pg.draw.circle(screen, color, (moves[i][1][0] * 100 + 351, moves[i][1][1] * 100 + 67), 5)
        #screen.blit(font.render('rook', True, 'black), (moves[i][1][0] * 100 + 351, moves[i][1][1] * 100 + 67))     

def Easy_Castle():
    pass

def draw__easy_castle():
    pass



''' Wait until able to make toggle for on/off for en Passant
def en_Passant(old_coor, new_coor):
    if turn_select < 2:
        index = white_loc.index(old_coor)
        eP_coords = (new_coor[0], new_coor[1] + 1)
        piece = white_pieces[index]
    else:
        index = black_loc.index(old_coor)
        eP_coords = (new_coor[0], new_coor[1] - 1)
        piece = black_pieces[index]

    if piece == 'pawn' and abs(old_coor[1] - new_coor[1]) > 1:
        pass
    else:
        eP_coords = (100, 100)

    return eP_coords    
'''


#Placeholder until checkmate and stalemate are finished
def Game_Over():
    status = [f"Game Over {winner.title()} wins!"]
    end_game = True
    Draw_Board(status)
    Draw_Pieces()
    Draw_Captured()

    return end_game


white_ops = check_ops(white_pieces, white_loc, 'white')
black_ops = check_ops(black_pieces, black_loc, 'black')
running = True
while running:
    timer.tick(fps)
    counter = counter + 1 if counter < 50 else 0  
    screen.fill("darkgreen")  

    Draw_Board(status)
    Draw_Pieces()
    Draw_Captured()
    Check()

    if not end_game:
        white_promote, black_promote, promote_index = Promotion()
        if white_promote or black_promote:
            draw_promotion()
            promotion_select()

    if selection != 100:
        valid_moves = check_valid()
        draw_moves(valid_moves)
        if select_piece == 'king':
            draw_castle(castle_moves)

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x_coor = event.pos[0] // 100 - 3
            y_coor = (event.pos[1] - 15) // 100
            clk_coor = (x_coor, y_coor)

            #For White
            if turn_select < 2:
                if clk_coor in white_loc:
                    selection = white_loc.index(clk_coor)
                    select_piece = white_pieces[selection]

                    if turn_select == 0:
                        turn_select = 1

                if clk_coor in valid_moves and selection != 100:
                    #white_eP = en_Passant(white_loc[selection], clk_coor)
                    white_loc[selection] = clk_coor
                    white_moved[selection] = True

                    if clk_coor in black_loc:
                        black_piece = black_loc.index(clk_coor)
                        captured_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        
                        black_pieces.pop(black_piece)
                        black_loc.pop(black_piece)
                        black_moved.pop(black_piece)
                    
                    #if clk_coor == black_eP:
                    #    black_piece = black_loc.index((black_eP[0], black_eP[1] + 1))
                    #    captured_white.append(black_pieces[black_piece])
                    #    
                    #    black_pieces.pop(black_piece)
                    #    black_loc.pop(black_piece)
                    #    black_moved.pop(black_piece)

                    #turn_end(black_pieces, black_loc, white_pieces, white_loc)
                    black_ops = check_ops(black_pieces, black_loc, 'black')
                    white_ops = check_ops(white_pieces, white_loc, 'white')
                    turn_select = 2
                    selection = 100
                    valid_moves = []
            
                elif selection != 100 and select_piece == 'king':
                    for q in range(len(castle_moves)):
                        if clk_coor == castle_moves[q][0]:
                            white_loc[selection] = clk_coor
                            white_moved[selection] = True
                            if clk_coor == (6, 7):
                                rook_coors = (7, 7)
                            else:
                                rook_coors = (0, 7)
                            rook_index = white_loc.index(rook_coors)
                            white_loc[rook_index] = castle_moves[q][1]

                            #turn_end(black_pieces, black_loc, white_pieces, white_loc)
                            black_ops = check_ops(black_pieces, black_loc, 'black')
                            white_ops = check_ops(white_pieces, white_loc, 'white')
                            turn_select = 2
                            selection = 100
                            valid_moves = []

            #For Black
            if turn_select >= 2:
                if clk_coor in black_loc:
                    selection = black_loc.index(clk_coor)
                    select_piece = white_pieces[selection]

                    if turn_select == 2:
                        turn_select = 3

                if clk_coor in valid_moves and selection != 100:
                    #black_eP = en_Passant(black_loc[selection], clk_coor)
                    black_loc[selection] = clk_coor
                    black_moved[selection] = True

                    if clk_coor in white_loc:
                        white_piece = white_loc.index(clk_coor)
                        captured_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'

                        white_pieces.pop(white_piece)
                        white_loc.pop(white_piece)
                        white_moved.pop(white_piece)

                    #if clk_coor == white_eP:
                    #    white_piece = white_loc.index((white_eP[0], white_eP[1] - 1))
                    #    captured_black.append(white_pieces[white_piece])
                    #    
                    #    white_pieces.pop(white_piece)
                    #    white_loc.pop(white_piece)
                    #    white_moved.pop(white_piece)

                    #turn_end(black_pieces, black_loc, white_pieces, white_loc)
                    white_ops = check_ops(white_pieces, white_loc, 'white')
                    black_ops = check_ops(black_pieces, black_loc, 'black')
                    turn_select = 0
                    selection = 100
                    valid_moves = []

                elif selection != 100 and select_piece == 'king':
                    for q in range(len(castle_moves)):
                        if clk_coor == castle_moves[q][0]:
                            black_loc[selection] = clk_coor
                            black_moved[selection] = True
                            if clk_coor == (1, 0):
                                rook_coors = (7, 0)
                            else:
                                rook_coors = (0, 0)
                            rook_index = black_loc.index(rook_coors)
                            black_loc[rook_index] = castle_moves[q][1]

                            #turn_end(black_pieces, black_loc, white_pieces, white_loc)
                            black_ops = check_ops(black_pieces, black_loc, 'black')
                            white_ops = check_ops(white_pieces, white_loc, 'white')
                            turn_select = 0
                            selection = 100
                            valid_moves = []

    if winner != '':
        checkmate = True
        turn_select = 0
        Game_Over()
    pg.display.flip()
pg.quit()
