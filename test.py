t = input("vad heter du? ")
print(f'du angav {t} som är {len(t)} tecken långt')
k = ""
o = list(t)
for item in o:
    if item == 'i':
        item = 1
    elif item == 'a':
        item = 4
    print(item)
    k = k + item
print(k)
