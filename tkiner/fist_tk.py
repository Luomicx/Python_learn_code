import tkinter as tk

root = tk.Tk()

root.title("我的第一个GUI程序")

root.geometry('500x300+100+100')

label = tk.Label(root, text="我的第一个tkinter窗口")

label.pack()

root.mainloop()