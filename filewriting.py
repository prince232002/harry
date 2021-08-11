f = open("harry.txt", "rt") #filename,mode(default rt)
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# it will print the each line in f and bydefault it also print bydefault a new line a also prints that's why we use end=""
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close() #refrigrator khola hai toh band krna padega 

# readlines- to store the whole string as list also include /n if a new is present 
# readline-read a single line 