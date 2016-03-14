# This program is based on my own module MiniGUI.py
# This program can run on 4 different modes, each mode is according to one of the homework3
# Writen by Wentao Liu, last modified on 2016/03/11

import math
import MiniGUI


RUN_MODE = 1            # run mode
WRITE_ROWS = 2          # the rows number when writing big charaters
WRITE_COLS = 10         # the columns number when writing big charaters
PAINT_WIDTH = 100       # the width when painting image
PAINT_HEIGHT = 33       # the height when painting image
ROTATE_SPEED = 0.2      # rotation speed
MOVING_SPEED = [1, 0]   # moving velocity

# some strange image
image = {"bus" : "\
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
@@            no time to explain!!               @@\n\
@@          quickly get on the bus!!             @@\n\
@@                                       00000   @@\n\
@@                                       0   0   @@\n\
@@                                       0   0   @@\n\
@@                                       00000   @@\n\
@@                                               @@\n\
@@                                               @@\n\
@@@@@@                                       @@@@@@", \
"wheel" : "\
  *****\n\
 *******\n\
*********\n\
*********\n\
*********\n\
*********\n\
********\n\
 ******\n\
  ****", \
"haha" : "\
                        . ...\n\
                   .............\n\
             .,::::,:,,,,,,,,,,,:::::..\n\
           ,::::.,,,.,.,...,.,.,.,.,,:::.\n\
         ,:::.,.,...,.............,.,.,,::,\n\
       ,:,.. ....................... . ..,,:.\n\
      ,,:i777;i:,   ...........   .:iiri::,.,.\n\
     LFE5uvv7LJ1FX2r.  .....   iuNk1YJYj2FXPu7,\n\
   ,E7,           :LOU.   .  ,U7:           i2@2\n\
  7@i                7Bi    5@,                2@\n\
 7@B@B7  :Lu15XF2L:    B:  B@B@B.  :7j115UUr.   :B\n\
 @B@B@BXqj7i,,..,i2@i  :B :@B@B@Bukuri::,:iLMO   2r\n\
 u@B@Bq:  .......  .GqrGj  B@B@B1.    .....  7@j:Bi\n\
  .:,  ..,...,.....  ,;:    .:.   ...,...,.,...rYr \n\
i.. ....,,,.,.,......   ...     ....,.,.,,,,,.,...,\n\
:,::,:,:,,,,.,.,.,.................,.,.,,,,:,:,:::,\n\
i,:::,:::,,,,,,.,.,.,.........,...,.,.,.,,,,:::,:::\n\
,:::::,:,:,:,,.,.,.,.........,.,.,.,.,,:,:,:,,::::,\n\
 ::iP.,,:,:,,,,,,.,.,.,.,.,.,.,.,.,.,,,,,,:,,.JL,i.\n\
 .i:X:.:,:::,:,:,:,,.,.,.,.,.,.,.,,,,,,:::,:,.Si:r\n\
  ;,vj.,:,:,:,:,:,:,,.,,,,,,,,,,,,:,,,:::::,.r5.i:\n\
  .r,27.,:,:::,:,:,:,,,:,:,,,:,,,:,:,:::::,.:0::;\n\
   ,;:Fv,,:::::,:,:,:,:,,,,,:,:,:::::::::,.iPi:r.\n\
    ,r:jui.:::::,:::::,:,:,:,:,:::::::::.:v2::;.\n\
     .r:ruYi:,:::::::::::::::::::::::,,:vuv:ii\n\
       :i:ruY7::,:,:::::::::::,:::,::rLu7::r:\n\
        .:i:i7YLvri::,,,,,,,:,::i;vLuv;:iii\n\
          .:ii:irvvJLLvv7v7vvLLJLvri:iii:.\n\
             .iir:::::ii;i;iii::::ii;:.\n\
                   ..,,:.,,,.,.,.."}


# recieve input to change mode
def change_mode():
    try:
        mode = raw_input("Enter the run_mode(0-3): ")[0]
    except:
        pass
    if mode == '0':
        run_mode0()
    elif mode == '1':
        run_mode1()
    elif mode == '2':
        run_mode2()
    elif mode == '3':
        run_mode3()


# run mode 0
def run_mode0():
    global canvas
    canvas = MiniGUI.Canvas(PAINT_WIDTH, PAINT_HEIGHT)
    canvas.draw_line("zi ji qu kan a ", [int(canvas.width * 0.4), 1])
    canvas.draw_image(image["haha"], [int(canvas.width * 0.2), 2])
    canvas.update()
    change_mode()


# run mode 1
def run_mode1():
    global canvas
    canvas = MiniGUI.Tablet(WRITE_ROWS, WRITE_COLS)
    canvas.draw_line("Welcome!", [int(canvas.width * 0.45), 1])
    canvas.draw_line("0.read the source code", [int(canvas.width * 0.3), 2])
    canvas.draw_line("1.homework_level1: here is", [int(canvas.width * 0.3), 3])
    canvas.draw_line("2.homework_level2: print any upper case on screen", [int(canvas.width * 0.3), 4])
    canvas.draw_line("3.homework_level3: let it be dynamic", [int(canvas.width * 0.3), 5])
    canvas.draw_line("Please enter 0-3 to select", [int(canvas.width * 0.3), 7])
    canvas.draw_text("LWT", [int(canvas.width * 0.35), 10])
    canvas.update()
    change_mode()


# run mode 2
def run_mode2():
    global canvas
    canvas = MiniGUI.Tablet(WRITE_ROWS, WRITE_COLS)
    try:
        canvas.draw_text(raw_input("Enter any number of upper case: ").upper())
    except KeyboardInterrupt:
        pass
    canvas.update()
    change_mode()


# run mode 3
def run_mode3():
    global canvas
    det_angle = 0
    det_pos = [0, 0]
    canvas = MiniGUI.Canvas(PAINT_WIDTH, PAINT_HEIGHT)
    while True:
        det_angle += math.pi * ROTATE_SPEED
        det_angle %= math.pi * 2
        det_pos[0] += MOVING_SPEED[0]
        det_pos[1] += MOVING_SPEED[1]
        det_pos[0] %= PAINT_WIDTH
        det_pos[1] %= PAINT_HEIGHT
        canvas.draw_image(image["wheel"], [5 + int(det_pos[0]), 5 + int(det_pos[1])], det_angle)
        canvas.draw_image(image["wheel"], [35 + int(det_pos[0]), 5 + int(det_pos[1])], det_angle)
        canvas.draw_image(image["bus"], [1 + int(det_pos[0]), 1 + int(det_pos[1])])
        canvas.draw_image("#########", [30, 25], det_angle)
        canvas.draw_image("#########", [60, 25], det_angle)
        canvas.update()


def run():
    run_mode1()


# create Canvas object
canvas = MiniGUI.Canvas(1, 1)
# run the program
run()