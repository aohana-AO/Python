from tkinter import *
from tkinter import ttk

root = Tk()
root.title('なまえ')

frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='君の名は')
moji = StringVar()
entry1 = ttk.Entry(frame1, textvariable=moji)
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('こんにちわ, %s.' % moji.get()))
# レイアウト
frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

# ウィンドウの表示開始
root.mainloop()
