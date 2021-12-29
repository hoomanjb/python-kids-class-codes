a = input("enter the sample sentence: ")
b = ["bad", "horrible", "disgust"]
c = ""
if a in b:
    d = a.replace('bad', "****")
    print(d)
else:
    print("the word does not exist in the sentence")
