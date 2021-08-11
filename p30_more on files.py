f = open("harry.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  
# seek()- point the file pointer at the desired character then start reading from their
# tell()-tell position of the file pointer   