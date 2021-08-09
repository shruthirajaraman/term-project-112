'''
- polygon collision
- reflecting over axes
- start with tesellations
- intersecting shapes: you can just get rid of the intersecting part with white 
so you don't have to worry about filling it anymore
Things to work on for tomorrow (8/9):
- Try to figure out how to fill a shape with a certain color <--
- Work on how to make a tesellation
'''
############
'''
IDEA FOR MAKING FILL COLORS:
- Make the tesellations and each time you do, store the corners of the shape 
into a list as another list (so you would have app.shapes be a 2D list)
- Write the function shapedClicked to figure out what list the event.x and 
event.y fall under
- In redrawAll, if specific x's and y's are satisfied, you can set the fill color

'''
'''
def drawHexagonTessellation(app, canvas):
    if app.hexagonSelected:
        for row in range(app.rows):
            for col in range(app.cols):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_polygon(x0, (y0 + y1) / 2, x0 + ((x1 - x0) / 4), 
                                    y0, x1 - ((x1 - x0) / 4), y0, x1, 
                                    (y0 + y1) / 2, x1 - ((x1 - x0) / 4), y1, 
                                    x0 + ((x1 - x0) / 4), y1, fill="white", 
                                    outline="black")

def drawTriangleTessellation(app, canvas):
    if app.triangleSelected:
        for row in range(app.rows - 1):
            for col in range(app.cols):
                for piece in range(4):
                    (x0, y0, x1, y1) = getCellBounds(app, row, col)
                    (vx0, vy0) = (x0, y0)
                    (vx1, vy1) = (x1 - ((x1 - x0) / 4), y0)
                    (vx2, vy2) = (x1 - ((x1 - x0) / 4), y0 + ((y1 - y0) / 4))
                    (vx3, vy3) = ((x0 + x1) / 2, y0 + ((y1 - y0) / 4))
                    (vx4, vy4) = ((x0 + x1) / 2, (y0 + y1) / 2)
                    (vx5, vy5) = (x0 + ((x1 - x0) / 4), (y0 + y1) / 2)
                    (vx6, vy6) = (x0 + ((x1 - x0) / 4), y0 + ((y1 - y0) / 4))
                    (vx7, vy7) = (x0, y0 + ((y1 - y0) / 4))
                    canvas.create_polygon(vx0, vy0, vx1, vy1, vx2, vy2, vx3, 
                                          vy3, vx4, vy4, vx5, vy5, vx6, vy6,
                                          vx7, vy7, fill="white", outline="black")
                    (vx0, vy0) = rotateByDegrees(vx0, vy0, math.pi/2)
                    (vx1, vy1) = rotateByDegrees(vx1, vy1, math.pi/2)
                    (vx2, vy2) = rotateByDegrees(vx2, vy2, math.pi/2)
                    (vx3, vy3) = rotateByDegrees(vx3, vy3, math.pi/2)
                    (vx4, vy4) = rotateByDegrees(vx4, vy4, math.pi/2)
                    (vx5, vy5) = rotateByDegrees(vx5, vy5, math.pi/2)
                    (vx6, vy6) = rotateByDegrees(vx6, vy6, math.pi/2)
                    (vx7, vy7) = rotateByDegrees(vx7, vy7, math.pi/2)
'''

from cmu_112_graphics import *
import math

def rotateByDegrees(x, y, theta):
    newX = (x * math.cos(theta)) - (y * math.sin(theta))
    newY = (x * math.sin(theta)) + (y * math.cos(theta))
    return (newX, newY)

def redrawAll(app, canvas):
    # canvas.create_rectangle(200, 250, 400, 350, fill="red")
    (x0, y0) = rotateByDegrees(200, 250, math.pi/2)
    (x1, y1) = rotateByDegrees(400, 350, math.pi/2)
    canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

runApp(width=600, height=600)