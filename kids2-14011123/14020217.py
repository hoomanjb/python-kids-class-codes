# import turtle as t
# import colorsys
# s = t.bgcolor('black')
# t.speed(0)
# a = 0
# b = 70
# for item in range(400):
#     c = colorsys.hsv_to_rgb(a, 1 ,0.8)
#     a += 1/b
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for item2 in range(2):
#         t.left(2)
#         t.circle(129)

# ###################################### #
# Python GUI Tkinter module

import tkinter as tk

window = tk.Tk('400x400')
# window2 = tk.Tk('500x500')
# widget:
# Label = نمایش متن در صفحه
# Button = ساخت دکمه
# Entry = وارد کردن متن در حداکثر یک خط
# Text = وارد کردن متن بیشتر از یک خط
# Frame = ساخت فریم در صفحه

# red orange yellow - #34A2FE (hexadecimal RGB code) (255, 255, 255) -> white --- (0, 0, 0) -> black

# anchor: w

# a = 'شسیشسی'
# text1 = tk.Label(text=a + '\n' + a + '\n' + a + '\n',
#                  foreground='white', background='#34A2FE',
#                  width=30, height=10, anchor='n', font=('Arial', 20))
# text2 = tk.Label(text='hello', fg='white', bg='#34A2FE')
#
# text1.pack()
# text2.pack()

# button = tk.Button(text='Click ME!', width=25, height=30,
#                    bg='pink', fg='green')
# button.pack()
# text = tk.Label(text='UserName', font=('Arial', 30))
# text.pack()
# entry = tk.Entry(fg='red', bg='white', width=50, font=('Arial', 30))
# entry.pack()

# text_box = tk.Text()
# text_box.pack()

# frame1 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
# frame2 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
# label = tk.Label(master=frame1, text='salammmmmmmmm')
# button = tk.Button(master=frame1, text='Click ME!')
# label2 = tk.Label(master=frame2, text='salammmmmmmmm2222')
# frame1.pack(side=tk.LEFT)
# label.pack()
# button.pack()
#
# frame2.pack(side=tk.LEFT)
# label2.pack()

# button_type = {
#     'flat': tk.FLAT, 'sunken': tk.SUNKEN, 'raised': tk.RAISED,
#     'groove': tk.GROOVE, 'ridge': tk.RIDGE
# }
#
# for key, value in button_type.items():
#     frame = tk.Frame(master=window, relief=value, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=key)
#     label.pack()

# frame1.pack(fill=tk.X)
# frame1.pack(fill=tk.Y, side=tk.LEFT)

# frame1 = tk.Frame(master=window, width=100, height=100, bg="blue")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="white")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="red")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)



# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()

# label1 = tk.Label(master=frame, text='salaaam chetoriiii', bg='red')
# label1.place(x=0, y=0)
#
# label2 = tk.Label(master=frame, text='salaaam chetoriiii 22222', bg='red')
# label2.place(x=60, y=60)


# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()



for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
# window2.mainloop()