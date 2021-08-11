# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
# d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs" #adding element to the dict
print(d2)
del d2[420]   #deleting element 
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
print(d2.item())
# for update dict ->>
# dict['key']=value
d2["Harry"]=33          
print(d2)