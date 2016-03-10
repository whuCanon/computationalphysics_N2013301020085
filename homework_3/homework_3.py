# import os
# import time
import MiniGUI


RUN_MODE = 1


def change_mode(mode):
    global RUN_MODE
    if mode == '0':
        RUN_MODE = 0
    elif mode == '1':
        RUN_MODE = 1
    elif mode == '2':
        RUN_MODE = 2
    elif mode == '3':
        RUN_MODE = 3


def run_mode0():
    pass


def run_mode1():
    MiniGUI.Canvas.REFRESH_RATE = 1
    x.draw_Line("Welcome!", [1, x.cols * 0.45])
    x.draw_Line("0.read the source code", [2, x.cols * 0.3])
    x.draw_Line("1.homework_level1: here is", [3, x.cols * 0.3])
    x.draw_Line("2.homework_level2: print any upper case on screen", [4, x.cols * 0.3])
    x.draw_Line("3.homework_level3: let it be dynamic", [5, x.cols * 0.3])
    x.draw_Line("Please enter 0-3 to select",[6, x.cols * 0.3])
    x.draw_Text("LWT", [10, x.cols * 0.35])
    x.update()
    try:
        change_mode(raw_input()[0])
    except:
        pass


def run_mode2():
    pass


def run_mode3():
    pass


def run():
    # main loop
    while True:
        if RUN_MODE == 0:
            run_mode0()
        elif RUN_MODE == 1:
            run_mode1()
        elif RUN_MODE == 2:
            run_mode2()
        elif RUN_MODE == 3:
            run_mode3()


# creat a new canvas
x = MiniGUI.Tablet(25, 100)
# run the program
run()