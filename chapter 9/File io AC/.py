f = open("demo.txt", "r")

data = f.read()
print(data)
line1 = f.readline() #nothing would be printed,Since the file pointer is at the end, calling f.readline() returns an empty string, indicating there’s no more content left to read.
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close