from gasp import *

LIGHTBLUE = "#03bafc"
GRAPHIC_WIDTH = 1750
GRAPHIC_HEIGHT = 1000

def horizon():
    Box((0, 0), GRAPHIC_WIDTH, GRAPHIC_HEIGHT / 2, True, color.GREEN)
    Box((0, GRAPHIC_HEIGHT / 2), GRAPHIC_WIDTH, GRAPHIC_HEIGHT / 2, True, LIGHTBLUE)

def meter(center):
    Circle(center, 50,True,color.DARKGRAY)
    Circle(center, 40,True,color.LIGHTGRAY)
    Line(center, (center[0], center[1] + 10), color.WHITE)

def height_meter(center):
    Arc(center, 20,0, 180, True,LIGHTBLUE, 40)
    Line((center[0]+10, center[1]),(center[0]-10, center[1]), color.RED)

def airspeed_visualiser(center):
    Line(center[0]+10, center[1]),(center[0]-10, center[1]), color.WHITE

def cessna172cockpit():
    controlsCorner = (GRAPHIC_WIDTH / 4,GRAPHIC_HEIGHT / 4)
    border = 70
    Box(controlsCorner , GRAPHIC_WIDTH / 2,GRAPHIC_HEIGHT / 2,True,color.GRAY)
    for row in range(3):
        for col in range(4):
            meter((controlsCorner[0] + border + col*130, controlsCorner[1] + border + row*130))
    height_meter((controlsCorner[0] + border, controlsCorner[1] + border))

#    Arc((110,320), 105, 270, 0, True, color.BLACK)

begin_graphics(GRAPHIC_WIDTH, GRAPHIC_HEIGHT)
horizon()
cessna172cockpit()
update_when('key_pressed')
end_graphics()