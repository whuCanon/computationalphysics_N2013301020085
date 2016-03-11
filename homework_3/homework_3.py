# import os
# import time
import MiniGUI


RUN_MODE = 1
WRITE_ROWS = 2    # < 3
WRITE_COLS = 10
PAINT_WIDTH = 100
PAINT_HEIGHT = 25


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
    canvas.draw_Line("Welcome!", [1, int(canvas.width * 0.45)])
    canvas.draw_Line("0.read the source code", [2, int(canvas.width * 0.3)])
    canvas.draw_Line("1.homework_level1: here is", [3, int(canvas.width * 0.3)])
    canvas.draw_Line("2.homework_level2: print any upper case on screen", [4, int(canvas.width * 0.3)])
    canvas.draw_Line("3.homework_level3: let it be dynamic", [5, int(canvas.width * 0.3)])
    canvas.draw_Line("Please enter 0-3 to select", [7, int(canvas.width * 0.3)])
    canvas.draw_Text("LWT", [10, int(canvas.width * 0.35)])
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
    canvas = MiniGUI.Canvas(PAINT_WIDTH, PAINT_HEIGHT)
    try:
        canvas.draw_image(raw_input()[ : -1], [2, 2])
    except KeyboardInterrupt:
        pass
    canvas.update()


def run():
    run_mode1()


# creat a new canvas
canvas = MiniGUI.Tablet(1, 1)
# run the program
run()
