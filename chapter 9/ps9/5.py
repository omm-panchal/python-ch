Words=["Turtle", "dheema", "panthi"]

with open("file.txt") as f:
    content =f.read()
for word in Words  :
  
  content = content.replace(word,"#"*len(Words))
with open("file.txt","w") as f:
  f.write(content)