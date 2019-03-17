from odroid_go import GO
from Entities.Block import Block
from Entities.Snake import Snake

SNAKE_COLOR = GO.lcd.colors.GREEN
BACKGROUND_COLOR = GO.lcd.colors.BLACK
FOOD_COLOR = GO.lcd.colors.RED
BORDER_COLOR = GO.lcd.colors.WHITE

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
BLOCK_SIZE = 10

#Where borders are drawn
INIT_X = 0
INIT_Y = 20

#Initial position of snake; relative to borders
SNAKEINIT_X = 40
SNAKEINIT_Y = 10

#Initial direction of snake
INITIALDIRECTION = 4

#Directions
#1: Forward
#2: Backward
#3: Left
#4: Right

def FillRectangle(block,color):
    GO.lcd.fill_rectangle(block.x,block.y,block.width,block.length,color)

def FillRectangles(blocks,color):
    for block in blocks:
        GO.lcd.fill_rectangle(block.x,block.y,block.width,block.length,color)

def DrawSnake(snake): 
    FillRectangle(snake.Head,SNAKE_COLOR)
    if not snake.BlockBehindTail == None:
        FillRectangle(snake.BlockBehindTail,BACKGROUND_COLOR)
