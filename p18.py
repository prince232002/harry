# i=0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1,end=" ")
#     if(i==41):
#         break  #stop
#     i=i+1

while(1):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue

