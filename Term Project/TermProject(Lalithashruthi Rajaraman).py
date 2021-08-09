#################################################
# Term Project
#
# Your name: Shruthi Rajaraman
# Your andrew id: lrajaram
#################################################

from cmu_112_graphics import *
import math

##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = "splashScreenMode"
    url = "https://tinyurl.com/47wprm59"
    # Background Image from https://tinyurl.com/676nekdw
    app.mandalaBG = app.loadImage(url)
    
    app.fillColor = "white"
    app.shapes = []

    app.hexagonSelected = False
    app.arrowSelected = False
    app.plusSelected = False

    app.rows = 8
    app.cols = 8

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def getCellBounds(app, row, col):
    cellWidth = app.width / app.cols
    cellHeight = app.height / app.rows
    x0 = cellWidth * col
    y0 = cellHeight * row
    x1 = x0 + cellWidth
    y1 = y0 + cellHeight
    return (x0, y0, x1, y1)

# Inspiration from https://tinyurl.com/5yzzuucp
def rotateByDegrees(x, y, theta):
    newX = (x * math.cos(theta)) - (y * math.sin(theta))
    newY = (x * math.sin(theta)) + (y * math.cos(theta))
    return (newX, newY)

def shapeClicked(app, x, y):
    pass

##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_mousePressed(app, event):
    if (event.x > app.width / 2 - 100 and event.x < app.width / 2 + 100 and
        event.y > app.height / 2 - 50 and event.y < app.height / 2):
        app.mode = "selectionMode"
    elif (event.x > app.width / 2 - 100 and event.x < app.width / 2 + 100 and
          event.y > app.height / 2 + 50 and event.y < app.height / 2 + 100):
        app.mode = "helpMode"

def drawGameTitle(app, canvas):
    canvas.create_rectangle(app.width / 2 - 200, app.height / 4 - 60, 
                            app.width / 2 + 200, app.height / 4 + 30, 
                            fill="pink")
    canvas.create_text(app.width / 2, app.height / 4, 
                       text="Patterns and Colors", 
                       font="Papyrus 32 bold", anchor="s")
    canvas.create_text(app.width / 2, app.height / 4 + 10, 
                       text="Take some time to relax and color beautiful patterns!", 
                       font="Papyrus 15 bold")

def drawButtons(app, canvas):
    # Play Button
    canvas.create_rectangle(app.width / 2 - 100, app.height / 2 - 50, 
                            app.width / 2 + 100, app.height / 2, 
                            fill="paleTurquoise")
    canvas.create_text(app.width / 2, app.height / 2 - 25, 
                       text="Start Coloring!", font="Courier 18")
    # How to Play Button
    canvas.create_rectangle(app.width / 2 - 100, app.height / 2 + 50, 
                            app.width / 2 + 100, app.height / 2 + 100, 
                            fill="paleTurquoise")
    canvas.create_text(app.width / 2, app.height / 2 + 75, 
                       text="How to Play", font="Courier 18")

def splashScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width / 2, app.height / 2, 
                        image=ImageTk.PhotoImage(app.mandalaBG))
    drawGameTitle(app, canvas)
    drawButtons(app, canvas)

##########################################
# Coloring Page Selection Mode
##########################################

def selectionMode_mousePressed(app, event):
    if distance(event.x, event.y, 37.5, 37.5) <= 18.75:
        app.mode = "splashScreenMode"
    elif (event.x > 10 and event.x < 180 and event.y > app.height / 2 - 85 and 
        event.y < app.height / 2 + 85):
        app.hexagonSelected = True
        app.mode = "coloringMode"
    elif (event.x > 215 and event.x < 385 and event.y > app.height / 2 - 85 and 
        event.y < app.height / 2 + 85):
        app.arrowSelected = True
        app.mode = "coloringMode"
    elif (event.x > 420 and event.x < 590 and event.y > app.height / 2 - 85 and 
        event.y < app.height / 2 + 85):
        app.plusSelected = True
        app.mode = "coloringMode"

def drawHexTessBox(app, canvas):
    canvas.create_rectangle(10, app.height / 2 - 85, 180, app.height / 2 + 85,
                            fill="pink")
    canvas.create_text(95, app.height / 2, text="   Hexagon\nTessellation",
                    font="Papyrus 20")

def drawArrowTessBox(app, canvas):
    canvas.create_rectangle(215, app.height / 2 - 85, 385, app.height / 2 + 85,
                            fill="pink")
    canvas.create_text(300, app.height / 2, text="     Arrow\nTessellation",
                    font="Papyrus 20")

def drawPlusTessBox(app, canvas):
    canvas.create_rectangle(420, app.height / 2 - 85, 590, app.height / 2 + 85,
                            fill="pink")
    canvas.create_text(505, app.height / 2, text="  Plus Sign\nTessellation", 
                       font="Papyrus 20")

def selectionMode_redrawAll(app, canvas):
    drawBackButton(app, canvas)
    drawHexTessBox(app, canvas)
    drawArrowTessBox(app, canvas)
    drawPlusTessBox(app, canvas)

##########################################
# Coloring Mode
##########################################

def coloringMode_mousePressed(app, event):
    pass 

def coloringMode_keyPressed(app, event):
    if (event.key == "Left"):
        app.hexagonSelected = False
        app.arrowSelected = False
        app.plusSelected = False
        app.mode = "selectionMode"
    # elif (event.key == "Space"):
    #     color = input("Pick a color! (all lowercase): ")
    #     print("color: " + color)
    #     app.fillColor = color

def drawHexagonTessellation(app, canvas):
    if app.hexagonSelected:
        for row in range(app.rows - 1):
            for col in range(app.cols):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_polygon((x0 + x1) / 2, y0, x1, 
                                    y0 + ((y1 - y0) / 4), x1, 
                                    y1 - ((y1 - y0) / 4), (x0 + x1) / 2, y1, 
                                    x0, y1 - ((y1 - y0) / 4), x0, 
                                    y0 + ((y1 - y0) / 4), fill="white", 
                                    outline="black")
                canvas.create_line(x0, y0 + ((y1 - y0) / 4), (x0 + x1) / 2, 
                                  (y0 + y1) / 2)
                canvas.create_line(x1, y0 + ((y1 - y0) / 4), (x0 + x1) / 2, 
                                  (y0 + y1) / 2)
                canvas.create_line((x0 + x1) / 2, y1, (x0 + x1) / 2, 
                                  (y0 + y1) / 2)

def drawArrowTessellation(app, canvas):
    if app.arrowSelected:
        for row in range(app.rows - 1):
            for col in range(app.cols):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_polygon(x0, (y0 + y1) / 2, x0 + ((x1 - x0) / 4), 
                                    y0, x0 + ((x1 - x0) / 4), y0 + 20, x1, 
                                    y0 + 20, x1, y1 - 20, x0 + ((x1 - x0) / 4), 
                                    y1 - 20, x0 + ((x1 - x0) / 4), y1, 
                                    fill="white", outline="black")

def drawPlusTessellation(app, canvas):
    if app.plusSelected:
        for row in range(app.rows - 1):
            for col in range(app.cols):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                (vx0, vy0) = (x0, y0 + ((y1 - y0) / 3))
                (vx1, vy1) = (x0 + ((x1 - x0) / 3), y0 + ((y1 - y0) / 3))
                (vx2, vy2) = (x0 + ((x1 - x0) / 3), y0)
                (vx3, vy3) = (x1 - ((x1 - x0) / 3), y0)
                (vx4, vy4) = (x1 - ((x1 - x0) / 3), y0 + ((y1 - y0) / 3))
                (vx5, vy5) = (x1, y0 + ((y1 - y0) / 3))
                (vx6, vy6) = (x1, y1 - ((y1 - y0) / 3))
                (vx7, vy7) = (x1 - ((x1 - x0) / 3), y1 - ((y1 - y0) / 3))
                (vx8, vy8) = (x1 - ((x1 - x0) / 3), y1)
                (vx9, vy9) = (x0 + ((x1 - x0) / 3), y1)
                (vx10, vy10) = (x0 + ((x1 - x0) / 3), y1 - ((y1 - y0) / 3))
                (vx11, vy11) = (x0, y1 - ((y1 - y0) / 3))
                canvas.create_polygon(vx0, vy0, vx1, vy1, vx2, vy2, vx3, 
                                        vy3, vx4, vy4, vx5, vy5, vx6, vy6,
                                        vx7, vy7, vx8, vy8, vx9, vy9, vx10, 
                                        vy10, vx11, vy11, 
                                        fill="white", outline="black")

def drawPaintBox(app, canvas):
    cellHeight = app.height / app.rows
    canvas.create_rectangle(0, app.height - cellHeight, app.width, app.height, 
                            fill="peach puff")
    canvas.create_text(app.width / 2, ((app.height * 2) - cellHeight) / 2, 
                       text="Here's where the paint goes!")

def coloringMode_redrawAll(app, canvas):
    drawHexagonTessellation(app, canvas)
    drawArrowTessellation(app, canvas)
    drawPlusTessellation(app, canvas)
    drawPaintBox(app, canvas)

##########################################
# Help Mode
##########################################

def helpMode_mousePressed(app, event):
    if distance(event.x, event.y, 37.5, 37.5) <= 18.75:
        app.mode = "splashScreenMode"

def drawBackButton(app, canvas):
    canvas.create_oval(10, 10, 65, 65, fill="pink")
    canvas.create_polygon(17, 37.5, 50, 20, 40, 37.5, 50, 55, 
                        fill="paleTurquoise", outline="black")

def drawInstructions(app, canvas):
    canvas.create_text(app.width / 2, app.height / 2, 
                       text="Here are where the instructions go!")

def helpMode_redrawAll(app, canvas):
    drawBackButton(app, canvas)
    drawInstructions(app, canvas)

runApp(width=600, height=600)