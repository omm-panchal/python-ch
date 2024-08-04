Word="Elephant"

with open("file.txt") as f:
    content =f.read()

with open("file.txt","w") as f:
  New_content = content.replace(Word,"########")
  f.write(New_content)