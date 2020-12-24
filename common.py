import  pygame as p
WIDTH = HEIGHT = 512
SQUARES = 8
SQ_SIZE = HEIGHT//SQUARES
MAX_FPS = 15
IMAGES = {}
def drawboard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(SQUARES):
        for col in range(SQUARES):
            color = colors[(row+col)%2]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE ))

def drawpieces(screen, board):
    for square_num in range(SQUARES * SQUARES):
        piece = str(board.piece_at(square_num))
        row = 7-square_num//8
        col = square_num%8
        if(piece != "None") : #empty square
            pieceimage = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE,SQ_SIZE))
            screen.blit(pieceimage, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
