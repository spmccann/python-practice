import string
import tkinter
from tkinter import ttk, Tk, END
import time

text = "Orville and Wilbur Wright started building gliders in " \
       "1900. In 1903, they built a motor and propeller for their glider. Orville made the first flight, which lasted " \
       "12 seconds, and flew 120 feet. Wilbur's flight was 852 feet in 59 seconds. These first flights in 1903 were " \
       "just the start of the evolution of planes."

count = 0
space = 0
start = time.time()


def key_strokes(event):
    global count
    global space
    count += 1
    end = time.time()
    total = end - start
    words_minute = count / total * 60 / 5
    key_press_minute = count / total * 60
    ttk.Label(frm, text=f"Keys/minute: {key_press_minute:.2f} \n WPM: {words_minute:.2f}").grid(column=0, row=1)
    if event.char == "O":
        w.tag_config("tag", underline=True)


window = Tk()
frm = ttk.Frame(window, padding=20)
frm.grid()
ttk.Label(frm, text="Typing Speed Test").grid(column=0, row=0)
r = tkinter.Text(state=tkinter.NORMAL, height=10)
r.grid(column=0, row=2)
r.insert(END, text)
w = tkinter.Text(state=tkinter.NORMAL)
w.grid(column=0, row=3)
w.bind("<Key>", key_strokes)
w.tag_add(tagName="tag", index1="1.0")
window.mainloop()
