with open("file.txt") as f:
    content = f.read()


with open("poem.txt") as f:
    content2 = f.read()    

if(content==content2)   :
    print("Both files are identical and same")
else:
       print("Both files aren't identical and same")