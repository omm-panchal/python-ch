with open("log.txt") as f:
   content = f.read()

   if "python" in content:
      print("yes python is in content")
   else:
            print("NO, python is not in content")