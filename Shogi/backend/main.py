import pygame as pg

pg.init()

width = 1500
height = 1000
screen = pg.display.set_mode([width, height])
pg.display.set_caption("Play Shogi 将棋")
font = pg.font.Font("freesansbold.ttf", 20)
big_font = pg.font.Font("freesansbold.ttf", 50)
timer = pg.time.Clock()
fps = 60
blocks = 9 ** 2


king_pieces = [
    'lance', 'knight', 'silver general', 'gold general', 'jade general', 'gold general', 'silver general', 'lance',
    'rook', 'bishop'
    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
king_loc = [
    (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7)
    (1,6), (6,6)
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5), (8,5)]

jadeGen_pieces = [
    'lance', 'knight', 'silver general', 'gold general', 'king', 'gold general', 'silver general', 'lance',
    'rook', 'bishop'
    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
jadeGen_loc = [ 
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0)
    (1,1),(7,1)
    (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2), (8,2)]

captured_white = []
captured_black = []

turn_select = 0
selection = 100
valid_moves = []