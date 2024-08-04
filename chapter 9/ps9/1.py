f = open("poem.txt")
content = f.read()
if("Twinkle"in content):
    print("Twinkle word is present in content ")
else :
    print("Twinkle word is absent in content ")


f.close()