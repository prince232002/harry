#list
grocery=["harpic","vim bar","deodrant",333]
# print(grocery[5])
number=[2, 4, 44, 21,55]
number.pop()    #delete last element from the list 
# number.sort()
# number.reverse()
# print(number)
# print(number[:3])  #list count from 1
# print(number[1:])  #start point not count
# print(number[1:5:-2]) #as blank string prints but aspected [7, 11] that's why we not use index -ve index less than 1 , its only do if there is no start and end eg. [::-3]
# print(number[::-3])
# some others- min ,max ,log etc
# number.append(1)
# number.append(122)
# number.insert(1,30)
number[1]=67    #replace the element by index value   
print(number)

# mutable- list and immutable -tuple
tp=(3,66)
# tp(1)
print(tp)

a=1
b=8
# general method for swap
# temp=a
# a=b
# b=temp
a,b=b,a
print(a,b)

# list comprehension
# newlist=[expresssion for in list if condition]
newlist =[i*3 for i in range(12) if i%2==0 ]
print(newlist)
