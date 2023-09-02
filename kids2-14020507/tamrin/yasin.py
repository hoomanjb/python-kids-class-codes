import tkinter
from tkinter.ttk import *

windows = tkinter.Tk()

windows.title("انبار داری یزدان بافت | pxc")

result = []


def show_result():
    new_window3 = tkinter.Tk()
    new_window3.title("نمایش نتایج | pxc")
    new_window3.geometry("1280x720")
    new_window3.mainloop()


def adding_resourse():
    #litri - kiloii - tedadi - mohemmat = 2 anbar -. anbar masrafi -> mavad avvalie
    new_window = tkinter.Tk()
    new_window.title("افزودن کالا | pxc")
    new_window.geometry("1280x720")

    combo = Combobox(new_window)
    combo["values"] = ("KG", "Liter", "Number")
    combo["state"] = "readonly"
    combo.current(2)
    combo.grid(column=1, row=0)
    c_val = combo.get()
    print(c_val)


    spin = Spinbox(new_window, from_=0, to=1000000000)
    spin.grid(column=0, row=0)


    new_window.mainloop()



def exporting_resource():
    new_window2 = tkinter.Tk()
    new_window2.title("ترخیص کالا | pxc")
    new_window2.geometry("1280x720")

    new_window2.mainloop()


bt1 = tkinter.Button(windows, height=3, width=15, text="افزودن کالا", bg="blue", fg="white", command=adding_resourse).pack()
l1 = tkinter.Label(text="یرای افزودن کالا لطفا روی دکمه بالا کلیک کنید").pack()
bt2 = tkinter.Button(windows, height=3, width=15, text="ترخیص کالا", bg="blue", fg="white", command=exporting_resource).pack()
l2 = tkinter.Label(text="برای ترخیص کالا روی دکمه بالا کلیک کنید").pack()
bt3 = tkinter.Button(windows, height=3, width=15, text="نمایش نتایج", bg="blue", fg="white", command=show_result).pack()
l3 = tkinter.Label(text="برای نمایش نتایج روی دکمه بالا کلیک کنید").pack()


windows.geometry("1280x720")
windows.mainloop()