import pygame as pg

jp_player_pieces = {
    "王将": "王",
    "飛車": "飛",
    "角行": "角",
    "金将": "金",
    "銀将": "銀",
    "桂馬": "桂",
    "香車": "香",
    "歩兵": "歩"
}
jp_player_flipped = {
    "龍王": "龍",
    "龍馬": "馬",
    "成銀": "全",
    "成桂": "圭",
    "成香": "杏",
    "と金": "と"
}
en_player_pieces = {
    "King": "K",
    "Rook": "R",
    "Bishop": "B",
    "Gold General": "G",
    "Silver General": "S",
    "Knight": "N",
    "Lancer": "L",
    "Pawn": "P"
}
en_player_flipped = {
    "Rook+": "+R",
    "Bishop+": "+B",
    "Silver+": "+S",
    "Knight+": "+N",
    "Lance+": "+L",
    "Tokin": "+P"
}
jp_com_pieces = {
    "玉将": "玉",
    "飛車": "飛",
    "角行": "角",
    "金将": "金",
    "銀将": "銀",
    "桂馬": "桂",
    "香車": "香",
    "歩兵": "歩"
}

#MAKE SURE TO Rename all pic FILEs FOR ALL THE IMGS AND PIECE LISTS

#NEED TO SET image.load() LOCATION TO PERSONAL FOLDER LOCATION
jgP = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgP.png'), (59.25, 83.25))
jgL = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgL.png'), (63.75, 85.5))
jgN = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgN.png'), (63.75, 85.5))
jgSG = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgSG.png'), (69.75, 87.75))
jgGG = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgGG.png'), (70.5, 88.5))
jgR = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgR.png'), (70.5, 88.5))
jgB = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgB.png'), (70.5, 88.5))

jgPp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgP+.png'), (59.25, 83.25))
jgLp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgL+.png'), (63.75, 85.5))
jgNp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgN+.png'), (63.75, 85.5))
jgSGp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgSG+.png'), (69.75, 87.75))
jgRp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgR+.png'), (70.5, 88.5))
jgBp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgB+.png'), (70.5, 88.5))
jgK = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/jgK.png'), (75, 90))



kP = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kP.png'), (59.25, 83.25))
kL = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kL.png'), (63.75, 85.5))
kN = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kN.png'), (63.75, 85.5))
kSG = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kSG.png'), (69.75, 87.75))
kGG = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kGG.png'), (70.5, 88.5))
kR = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kR.png'), (70.5, 88.5))
kB = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kB.png'), (70.5, 88.5))

kPp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kP.png'), (59.25, 83.25))
kLp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kL.png'), (63.75, 85.5))
kNp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kN.png'), (63.75, 85.5))
kSGp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kSG.png'), (69.75, 87.75))
kRp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kR.png'), (70.5, 88.5))
kBp = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kB.png'), (70.5, 88.5))
kK = pg.transform.scale(pg.image.load('Games/Shogi/backend/images/kK.png'), (75, 90))
