class car:
    wheels =4      #class variable as it is common to both object 
    def __init__(self):
        self.mil=10      #intances variable as they can change -mil and com
        self.com="bmw"
                           
c1=car()
c2=car()
c1.wheels=5
c1.mil=8
 

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)


# namespaces - where variables and object are stored  and created
# class namespaces
# object namespaces
