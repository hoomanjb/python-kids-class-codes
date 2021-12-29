b=input('enter your word')
x=["a",'e',"i","u",'o']
v=0
for letter in b:
    if letter in x:
        v+=1
print(v)
