import os
import time


class Canvas:
    REFRESH_RATE = 0.05
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.tupMatrix = {}

    def draw(self):
        tmp_str = ""
        for i in range(self.height):
            tmp_str = ""
            for j in range(self.width):
                if self.tupMatrix.has_key((i, j)):
                    tmp_str += self.tupMatrix[(i, j)]
                else:
                    tmp_str += " "
            print tmp_str

    def draw_Line(self, text, pos):
        cursor_pos = pos
        for ch in text:
            self.tupMatrix[tuple(cursor_pos)] = ch
            cursor_pos[1] += 1

    def draw_image(self, text, pos, angle = 0):
        image_width = 0
        image_height = 0
        cursor_pos = pos
        for ch in text:
            tmp_width = 0
            if ch != '\n':
                self.tupMatrix[tuple(cursor_pos)] = ch
                cursor_pos[1] += 1
                tmp_width += 1
            else:
                cursor_pos[0] += 1
                cursor_pos[1] = pos[1]
                image_height += 1
                if tmp_width > image_width:
                    image_width = tmp_width
        # rotate(image_width, image_height, pos, angle)


    def clear(self):
        self.tupMatrix.clear()

    def update(self):
        for i in range(self.height):
            self.tupMatrix[(i, 0)] = '|'
            self.tupMatrix[(i, self.width - 1)] = '|'
        for i in range(self.width):
            self.tupMatrix[(0, i)] = '='
            self.tupMatrix[(self.height - 1, i)] = '='
        os.system('cls')
        self.draw()
        self.clear()
        try:
            time.sleep(self.REFRESH_RATE)
        except KeyboardInterrupt:
            pass


class Tablet(Canvas):
    FONT_WIDTH = 9
    FONT_HEIGHT = 10
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

    def update(self):
        for i in range(self.height / self.FONT_HEIGHT):
            for j in range(self.width):
                self.tupMatrix[((i + 1) * self.FONT_HEIGHT, j)] = '-'
        Canvas.update(self)

    def draw_Text(self, text, pos = [0, 0]):
        str_len = len(text)
        for i in range(self.rows):
            for j in range(self.cols):
                if str_len == 0:
                    break
                try:
                    cursor_pos = [i * self.FONT_HEIGHT + pos[0] + 1, j * self.FONT_WIDTH + pos[1] + 1]
                    for ch in self.dict[text[-str_len]]:
                        if ch != '\n':
                            self.tupMatrix[tuple(cursor_pos)] = ch
                            cursor_pos[1] += 1
                        else:
                            cursor_pos[0] += 1
                            cursor_pos[1] = j * self.FONT_WIDTH + pos[1] + 1
                    str_len -= 1
                except KeyError:
                    self.draw_Line("only upper case!", [1, 1])

