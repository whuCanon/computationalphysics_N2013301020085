# This is a mini-GUI module which is based on terminal
# Writen by Wentao Liu, last modified on 2016/03/11

# to use this module, firstly create a new Canvas(with width and height, for painting),
# or Tablet(with rows and columns, for writting) as global variate.
# For Canvas, you can use draw_line() to draw a string to the virtual screen,
# or you can use draw_image() to draw a image in type matrix to the virtual screen.
# for Tablet, you can use draw_text() to draw a series of big character to the virtual screen.
# After draw*(), you need to use update() to print your virtual screen to the real screen.

# You should notice that the big character you can "draw_text()" are limited to the Tablet's dict.
# You can add your own big character to the dict, but remember don't be out of range

import os
import time
import math


class Canvas:
    ''' usage: canvas = MiniGUI.Canvas(width, height) '''
    REFRESH_RATE = 0.05     # the refresh rate of virtual screen, default is 1 / 0.05 = 20 per second
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.tupMatrix = {}

    # print the virtual screen to real screen
    def draw(self):
        tmp_str = ""
        for y in range(self.height):
            tmp_str = ""
            for x in range(self.width):
                if self.tupMatrix.has_key((x, y)):
                    tmp_str += self.tupMatrix[(x, y)]
                else:
                    tmp_str += " "
            print tmp_str

    def draw_line(self, text, pos):
        '''
        usage: canvas.draw_line("the text you want to print", [position_x,
        position_y])
        '''
        cursor_pos = pos
        for ch in text:
            self.tupMatrix[tuple(cursor_pos)] = ch
            cursor_pos[0] += 1

    def draw_image(self, text, pos, angle = 0):
        '''
        usage: canvas.draw_image("the text of image in type matrix", pos,
        rotation's_angle(is optional, default is 0))
        '''
        image_dict = {}
        image_width = 0
        image_height = 0
        cursor_pos = [pos[0], pos[1]]
        tmp_width = 0
        for ch in text:
            if ch != '&' and ch != '\r' and ch != '\n':
                image_dict[tuple(cursor_pos)] = ch
                cursor_pos[0] += 1
                tmp_width += 1
            else:
                cursor_pos[1] += 1
                cursor_pos[0] = pos[0]
                image_height += 1
                if tmp_width > image_width:
                    image_width = tmp_width
                tmp_width = 0
        if angle != 0:
            self.rotate(image_dict, image_width, image_height, pos, angle)
        self.tupMatrix.update(image_dict)

    def rotate(self, image_dict, width, height, pos, angle):
        ''' rotate the image '''
        tmp_dict = {}
        tmp_dict.update(image_dict)
        o_pos = [pos[0] + width / 2, pos[1] + height / 2]
        for point in tmp_dict:
            o_x = point[0] - o_pos[0]
            o_y = point[1] - o_pos[1]
            o_x_ = round(o_x * math.cos(angle) - o_y * math.sin(angle))
            o_y_ = round(o_x * math.sin(angle) + o_y * math.cos(angle))
            del image_dict[point]
            image_dict[(o_x_ + o_pos[0], o_y_ + o_pos[1])] = tmp_dict[point]

    def clear(self):
        ''' clear the virtual screen per frame '''
        self.tupMatrix.clear()

    def update(self):
        ''' update and print the real screen '''
        tmp_dict = {}
        tmp_dict.update(self.tupMatrix)
        for key in tmp_dict:
            if key[0] < 0 or key[0] > self.width or key[1] < 0 or key[1] > self.height:
                del self.tupMatrix[key]
                self.tupMatrix[(key[0] % self.width, key[1] % self.height)] = tmp_dict[key]
        del tmp_dict
        for i in range(self.height):
            self.tupMatrix[(0, i)] = '|'
            self.tupMatrix[(self.width - 1), i] = '|'
        for i in range(self.width):
            self.tupMatrix[(i, 0)] = '='
            self.tupMatrix[(i, self.height - 1)] = '='
        os.system('clear')
        self.draw()
        self.clear()
        try:
            time.sleep(self.REFRESH_RATE)
        except KeyboardInterrupt:
            pass


class Tablet(Canvas):
    ''' usage: tablet = MiniGUI.Tablet(rows, columns) '''
    FONT_WIDTH = 9      # the max width of the character
    FONT_HEIGHT = 10    # the max height of the character
    # some character's type matrix, you can add yourself
    dict = {
        'A': "\n   #     \n   ##    \n  # #    \n  #  #   \n  ####   \n #    #  \n###  ### \n", \
        'B': "\n######   \n #    #  \n ######  \n #     # \n #     # \n #     # \n#######  \n", \
        'C': "\n   ####  \n  #    # \n #       \n #       \n #       \n  #    # \n   ####  \n", \
        'D': "\n######   \n #    #  \n #     # \n #     # \n #     # \n #    #  \n######   \n", \
        'E': "\n######   \n #    #  \n #       \n ####    \n #       \n #    #  \n######   \n", \
        'F': "\n ####### \n  #      \n  #   #  \n  #####  \n  #   #  \n  #      \n ###     \n", \
        'G': "\n   ####  \n  #   #  \n #       \n #       \n #   ##  \n #    #  \n  #####  \n", \
        'H': "\n###  ### \n #    #  \n #    #  \n ######  \n #    #  \n #    #  \n###  ### \n", \
        'I': "\n #####   \n   #     \n   #     \n   #     \n   #     \n   #     \n #####   \n", \
        'J': "\n  #####  \n    #    \n    #    \n    #    \n    #    \n#   #    \n ###     \n", \
        'K': "\n##  ##   \n #  #    \n # #     \n ##      \n # #     \n #  #    \n##  ##   \n", \
        'L': "\n###      \n #       \n #       \n #       \n #       \n #    #  \n#######  \n", \
        'M': "\n ## ##   \n#######  \n#  #  #  \n#  #  #  \n#  #  #  \n#  #  #  \n#  #  #  \n", \
        'N': "\n##   ### \n ##   #  \n # #  #  \n #  # #  \n #   ##  \n #    #  \n###   #  \n", \
        'O': "\n  ###    \n #   #   \n#     #  \n#     #  \n#     #  \n #   #   \n  ###    \n", \
        'P': "\n######   \n #    #  \n #    #  \n #####   \n #       \n #       \n###      \n", \
        'Q': "\n  ###    \n #   #   \n#     #  \n#     #  \n#   # #  \n #   #   \n  ### ## \n", \
        'R': "\n######   \n #    #  \n #    #  \n #####   \n ###     \n #  #    \n###  ##  \n", \
        'S': "\n  #####  \n #    #  \n ##      \n   ##    \n     ##  \n #    #  \n #####   \n", \
        'T': "\n#######  \n   #     \n   #     \n   #     \n   #     \n   #     \n  ###    \n", \
        'U': "\n###  ### \n #    #  \n #    #  \n #    #  \n #    #  \n #    #  \n  ####   \n", \
        'V': "\n###  ### \n #    #  \n #    #  \n ##  #   \n  #  #   \n  #  #   \n   ##    \n", \
        'W': "\n## # ##  \n # # #   \n # # #   \n # # #   \n # # #   \n  ###    \n  # #    \n", \
        'X': "\n###  ### \n #    #  \n  #  #   \n   ##    \n   ##    \n  #  #   \n##    ## \n", \
        'Y': "\n### ###  \n #   #   \n #   #   \n  # #    \n   #     \n   #     \n  ###    \n", \
        'Z': "\n ######  \n#    #   \n    #    \n   #     \n  #      \n #    #  \n######   \n", \
        ' ': "\n         \n         \n         \n         \n         \n         \n         \n"
    }

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        Canvas.__init__(self, cols * self.FONT_WIDTH + 1, rows * self.FONT_HEIGHT + 1)

    def draw_text(self, text, pos = [0, 0]):
        ''' usage: tablet.draw_text("this must be in the dict!", [position_x, position_y]) '''
        str_len = len(text)
        for y in range(self.rows):
            for x in range(self.cols):
                if str_len == 0:
                    break
                try:
                    cursor_pos = [x * self.FONT_WIDTH + pos[0] + 1, y * self.FONT_HEIGHT + pos[1] + 1]
                    for ch in self.dict[text[-str_len]]:
                        if ch != '\n':
                            self.tupMatrix[tuple(cursor_pos)] = ch
                            cursor_pos[0] += 1
                        else:
                            cursor_pos[1] += 1
                            cursor_pos[0] = x * self.FONT_WIDTH + pos[0] + 1
                    str_len -= 1
                except KeyError:
                    self.draw_line("only upper case!", [1, 1])

    def update(self):
        for i in range(self.height / self.FONT_HEIGHT):
            for j in range(self.width):
                self.tupMatrix[(j, (i + 1) * self.FONT_HEIGHT)] = '-'
        Canvas.update(self)
