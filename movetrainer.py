from common import *
import  pygame as p
import chess
import chess.pgn
import chess.svg
import time


#board = chess.Board()
pgn = open("mygame.pgn")
game = chess.pgn.read_game(pgn)
board = game.board()


p.init()

screen = p.display.set_mode((WIDTH, HEIGHT))
screen.fill(p.Color("white"))
clock = p.time.Clock()
running = True
#while running:
for move in game.mainline_moves():
    clock.tick(MAX_FPS)
    drawboard(screen)
    drawpieces(screen,board)
    board.push(move)
    p.display.flip()
    time.sleep(1)