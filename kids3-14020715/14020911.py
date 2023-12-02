# Tkinter - python frameWrok GUI
import tkinter as tk

# window = tk.Tk()
# Label , Button , Entry , Text , Frame

# def show_entry():
#     print(entry.get())
#     return
#
# label1 = tk.Label(
#     text='Hello World', fg='yellow', bg='red',
#     width=10, height=10, justify='right'
# )
# label1.pack()
#
# button = tk.Button(
#     text='Click me!', width=25, height=10,
#     fg='red', command=show_entry
# )
# button.pack()
#
# entry = tk.Entry(width=50)
# entry.pack()
# entry.delete(1, 10)
# placeholder
# entry.insert(0, 'enter your name')

# frame1 = tk.Frame()
# frame2 = tk.Frame()

# label1 = tk.Label(master=frame1, text='salam az frame1')
# label1.pack()
#
# label2 = tk.Label(master=frame2, text='salam az frame 2')
# label2.pack()

# frame2.pack()
# frame1.pack()

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name, width=10, height=15)
#     label.pack()

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.X)


# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.Y, side=tk.LEFT)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.Y, side=tk.LEFT)


# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


# frame = tk.Frame(width=150, height=150)
# frame.pack()
# label1 = tk.Label(master=frame, text='man dar moghe 0, 0 hastam', bg='red')
# label1.place(x=0, y=0)
#
# label2 = tk.Label(master=frame, text='man dar moghe 70, 80 hastam', bg='blue')
# label2.place(x=70, y=80)

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


# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)

    # for j in range(0, 3):
    #     frame = tk.Frame(
    #         master=window,
    #         relief=tk.RAISED,
    #         borderwidth=1
    #     )
    #     frame.grid(row=i, column=j, padx=5, pady=5)
    #     label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    #     label.pack(padx=5, pady=5)

# window = tk.Tk()
# window.geometry('320x320')
# window.title('Calculator')
#
# input_text = tk.StringVar()
#
# def clear_all():
#     pass
#
# def back_space():
#     pass
#
# def divide():
#     pass
#
# entry = tk.Entry(textvariable=input_text, width=50)
# entry.grid(row=0, column=0)
#
# button_c = tk.Button(text='C', command=clear_all)
# button_c.grid(row=1, column=0)
# button_bs = tk.Button(text='<-', command=back_space)
# button_bs.grid(row=1, column=1)
# button_div = tk.Button(text='/', command=divide)
# button_div.grid(row=1, column=2)
#
# window.mainloop()



# import tkinter as tk
#
#
# def btn_click(numbers):
#     global operator
#     operator = operator + str(numbers)
#     text_input.set(operator) # 1 + 2
#
#
# def btn_clear_display():
#     global operator
#     operator = ''
#     text_input.set('')
#
#
# def btn_equal_input():
#     global operator
#     sumup = str(eval(operator))
#     text_input.set(sumup)
#     operator = ''
#
# cal = tk.Tk()
# cal.title("CALCULATOR")
# operator = ''
# text_input = tk.StringVar()
#
# text_display = tk.Entry(
#     cal, font=('arial', 20, 'bold'), textvariable=text_input,
#     bd=30, insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)
# # -------------------------------------
# btn_clear = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='C', bg='powder blue', command=btn_clear_display).grid(column=0, row=1)
#
# btn_m = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='M', bg='powder blue').grid(column=1, row=1)
#
# btn_bracket1 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='(', bg='powder blue', command=lambda: btn_click('(')).grid(column=2, row=1)
#
# btn_bracket2 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text=')', bg='powder blue', command=lambda: btn_click(')')).grid(column=3, row=1)
# # ----------------------------------------------------
# btn_7 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='7', bg='powder blue', command=lambda: btn_click('7')).grid(column=0, row=2)
#
# btn_8 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='8', bg='powder blue', command=lambda: btn_click('8')).grid(column=1, row=2)
#
# btn_9 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='9', bg='powder blue', command=lambda: btn_click('9')).grid(column=2, row=2)
#
# btn_divide = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='/', bg='powder blue', command=lambda: btn_click('/')).grid(column=3, row=2)
# # -------------------------------------------------
# btn_4 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='4', bg='powder blue', command=lambda: btn_click('4')).grid(column=0, row=3)
#
# btn_5 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='5', bg='powder blue', command=lambda: btn_click('5')).grid(column=1, row=3)
#
# btn_6 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='6', bg='powder blue', command=lambda: btn_click('6')).grid(column=2, row=3)
#
# btn_sub = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='-', bg='powder blue', command=lambda: btn_click('-')).grid(column=3, row=3)
# # ----------------------------------------------
# btn_1 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='1', bg='powder blue', command=lambda: btn_click('1')).grid(column=0, row=4)
#
# btn_2 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='2', bg='powder blue', command=lambda: btn_click('2')).grid(column=1, row=4)
#
# btn_3 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='3', bg='powder blue', command=lambda: btn_click('3')).grid(column=2, row=4)
#
# btn_multy = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='*', bg='powder blue', command=lambda: btn_click('*')).grid(column=3, row=4)
# # --------------------------------------
# btn_0 = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='0', bg='powder blue', command=lambda: btn_click('0')).grid(column=0, row=5)
#
# btn_dot = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='.', bg='powder blue', command=lambda: btn_click('.')).grid(column=1, row=5)
#
# btn_equal = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='=', bg='powder blue', command=btn_equal_input).grid(column=2, row=5)
#
# btn_add = tk.Button(
#     cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#     text='+', bg='powder blue', command=lambda: btn_click('+')).grid(column=3, row=5)
#
# cal.mainloop()


# show
# upload
#