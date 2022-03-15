from tkinter import *
from tkinter import ttk


class CalcApp(ttk.Frame):
    """電卓アプリ(予定)."""

    def __init__(self, master=None):
        super().__init__(master)




def main():
    root = Tk()
    root.title('電卓')
    CalcApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()