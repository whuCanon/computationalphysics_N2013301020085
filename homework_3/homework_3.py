# import os
# import time
import math
import MiniGUI


RUN_MODE = 1
WRITE_ROWS = 2    # < 3
WRITE_COLS = 10
PAINT_WIDTH = 100
PAINT_HEIGHT = 25
ROTATE_SPEED = 0.1


def change_mode(mode):
    if mode == '0':
        run_mode0()
    elif mode == '1':
        run_mode1()
    elif mode == '2':
        run_mode2()
    elif mode == '3':
        run_mode3()


def run_mode0():
    pass


def run_mode1():
    global canvas
    canvas = MiniGUI.Tablet(WRITE_ROWS, WRITE_COLS)
    canvas.draw_Line("Welcome!", [int(canvas.width * 0.45), 1])
    canvas.draw_Line("0.read the source code", [int(canvas.width * 0.3), 2])
    canvas.draw_Line("1.homework_level1: here is", [int(canvas.width * 0.3), 3])
    canvas.draw_Line("2.homework_level2: print any upper case on screen", [int(canvas.width * 0.3), 4])
    canvas.draw_Line("3.homework_level3: let it be dynamic", [int(canvas.width * 0.3), 5])
    canvas.draw_Line("Please enter 0-3 to select", [int(canvas.width * 0.3), 7])
    canvas.draw_Text("LWT", [int(canvas.width * 0.35), 10])
    canvas.update()
    try:
        change_mode(raw_input("Enter the run_mode(0-3): ")[0])
    except KeyboardInterrupt:
        pass


def run_mode2():
    global canvas
    canvas = MiniGUI.Tablet(WRITE_ROWS, WRITE_COLS)
    try:
        canvas.draw_Text(raw_input("Enter any number of upper case: ")[ : -1])
    except KeyboardInterrupt:
        pass
    canvas.update()
    try:
        change_mode(raw_input("Enter the run_mode(0-3): ")[0])
    except KeyboardInterrupt:
        pass


def run_mode3():
    global canvas
    angle = 0
    canvas = MiniGUI.Canvas(PAINT_WIDTH, PAINT_HEIGHT)
    try:
        image_text = raw_input("Enter an image in pixel matrix, use & to a new line:")[ : -1]
    except KeyboardInterrupt:
        pass
    while True:
        angle += math.pi * ROTATE_SPEED
        angle %= math.pi * 2
        canvas.draw_image(image_text, [40, 5], angle)
        canvas.update()


def run():
    run_mode1()


# creat a new canvas
canvas = MiniGUI.Tablet(1, 1)
# run the program
run()
