from tkinter import *

import file_load
import huffman

root = Tk()
root.title("Midas")
root.geometry("500x500")


class Elder:
    huff: huffman.Huffman = None

    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.pack()
        self.button_create = Button(master, text="create", command=self.create_huffman)
        self.button_create.pack()
        self.button_load = Button(master, text="load", command=self.start)
        self.button_load.pack()
        self.promp_win = Text(root, height=200, width=200)
        self.promp_win.pack()

    def create_huffman(self):
        tmp = self.get_prompt()
        tmp2 = file_load.data_load(tmp)
        if not tmp2[0]:
            self.say_board("err load file")
            return
        tmp3 = file_load.get_data(tmp2)
        if tmp3 is None:
            self.say_board("err compile file")
            return
        self.huff = huffman.Huffman(tmp3)
        self.clear_board()

    def start(self):
        if self.huff is None:
            self.say_board("need to create Huffman")
            return
        self.huff.calc()
        self.huff.get_res()
        self.say_board(self.huff.res)

    def get_prompt(self):
        return self.promp_win.get("1.0", "end-1c")

    def clear_board(self):
        self.promp_win.delete(1.0, "end")

    def say_board(self, text_s):
        self.clear_board()
        self.promp_win.insert(1.0, text_s)


e = Elder(root)
root.mainloop()
