import os
import time

REFRESH_RATE = 0.05
FONT_WIDTH = 9
FONT_HEIGHT = 10
dict = {
    'A': "\n   #     \n   ##    \n  # #    \n  #  #   \n  ####   \n #    #  \n###  ### \n", 'B': "\n######   \n #    #  \n ######  \n #     # \n #     # \n #     # \n#######  \n", "C": "\n   ####  \n  #    # \n #       \n #       \n #       \n  #    # \n   ####  \n", "D": "\n######   \n #    #  \n #     # \n #     # \n #     # \n #    #  \n######   \n", "E": "\n", "F": "\n ####### \n  #      \n  #   #  \n  #####  \n  #   #  \n  #      \n ###     \n", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""
}


class Canvas:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tupMatrix = {}

    def draw(self):
        tmp_str = ""
        for i in range(self.rows):
            tmp_str = ""
            for j in range(self.cols):
                if self.tupMatrix.has_key((i, j)):
                    tmp_str += self.tupMatrix[(i, j)]
                else:
                    tmp_str += " "
            print tmp_str

    def draw_Line(self, pos, text):
        cursor_pos = pos
        for ch in text:
            self.tupMatrix[tuple(cursor_pos)] = ch
            cursor_pos[1] += 1

    def clear(self):
        self.tupMatrix.clear()

    def update(self):
        self.draw()
        self.clear()
        time.sleep(REFRESH_RATE)
        os.system('cls')


class Tablet(Canvas):

    def __init__(self, rows, cols):
        Canvas.__init__(self, rows, cols)

    def update(self):
        for i in range(self.rows / FONT_HEIGHT):
            for j in range(self.cols):
                self.tupMatrix[((i + 1) * FONT_HEIGHT, j)] = '-'
        for i in range(self.rows):
            self.tupMatrix[(i, 0)] = '|'
            self.tupMatrix[(i, self.cols - 1)] = '|'
        for i in range(self.cols):
            self.tupMatrix[(0, i)] = '='
            self.tupMatrix[(self.rows - 1, i)] = '='
        Canvas.update(self)

    def draw_Text(self, text):
        str_len = len(text)
        char_rows = self.rows / FONT_HEIGHT
        char_cols = self.cols / FONT_WIDTH
        for i in range(char_rows):
            for j in range(char_cols):
                if str_len == 0:
                    break
                try:
                    cursor_pos = [i * FONT_HEIGHT + 1, j * FONT_WIDTH + 1]
                    for ch in dict[text[-str_len]]:
                        if ch != '\n':
                            self.tupMatrix[tuple(cursor_pos)] = ch
                            cursor_pos[1] += 1
                        else:
                            cursor_pos[0] += 1
                            cursor_pos[1] = j * FONT_WIDTH + 1
                    str_len -= 1
                except KeyError:
                    self.draw_Line([1, 1], "only upper case!")


# creat a new canvas
x = Tablet(25, 80)
# Welcomes
#x.draw_Line([x.cols / 2, 2], "Welcomes!!!")
# main loop
while True:
    x.draw_Text("a")
    x.update()
