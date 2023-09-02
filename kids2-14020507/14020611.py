# DataBase - NoSql, Sql
# query
# DB -> Python

# OOP - شی گرایی

# FrameWork = (Django - Flask - FastApi - web2py - Cherrypy - DjangoRest)
# Engine = Unreal - Unity

# Api - Method get post update

# Decorator
# async - sync
# log
# monitoring
# Solid
# Clean code
# Pandas
# Docker
# Git - مدیریت پروژس
# Github - Gitlab - bitbucket

# 80,000,000 sms
# eid mobarak.
# panel payamaki


# for item in range(80_000_000):
#     print('eid mobarak')
    # request -> panel -> user
    # wait save(response)
    # Delivery <- panel <- user
    # 5s
    # 5 * 80_000_000
    # async
    #

# monitoring

# ###########################################
# Tkinter
import tkinter as tk
window = tk.Tk()
window.geometry('400x400')


# Widget
# Lable -> namayesh matn
# Button -> dokme
# Entry -> vorodi tak  khati
# Text -> vorodi bisht az 1 khat
# Frame


# label = tk.Label(
#     text='', fg='white', bg='blue',
#     width=10, height=10, font=('Arial', 10)
# )
label = tk.Label(
    text='User Name', font=('Arial', 10)
)
label.pack()

def chert():
    global window
    name = entry.get()
    print(name)
    window.destroy()
    window = tk.Tk()

button = tk.Button(
    text='Click On me!', width=10, height=5,
    bg='red', command=chert
    )

entry = tk.Entry(fg='green', width=20)
entry.pack()
button.pack()


window.mainloop()
