print("list iteration")
I=["geeks","for","geeks"]
for i in I:
    print(i)
print("\nTuple Iteration")
t=("geeks","for","geeks")
for i in t:
    print(i)
print("\nString Iteration")
s = "Geeks"
for i in s :
    print(i)
for letter in 'geeksforgeeks':
    if letter=='e'or letter=='s':
            continue
    print ('Current Letter:'),letter
    var = 10
for letter in 'geeksforgeeks':
     if letter=='e' or letter =='s':
          break
print ('Current Letter:'),letter
def my_function(fname):
     print(fname + "Refsnes")
my_function("Emily")
my_function("Tobias")
my_function("Linus")
def my_function(country="Pakistan"):print("i am from"+ country)
my_function("Sweden")  
my_function("India")  
my_function()  
my_function("Brazil")

def my_function(food):
      for x in food:
           print(x)

fruits=["apple","Banana","cherry"] 
my_function(fruits)
def my_function(x):
     return 5*x

print(my_function(3)) 
print(my_function(5)) 
print(my_function(9)) 
def my_function(child3, child2, child1):
     print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
class Person:
    def __init__(self,name,age):
     self.name=name
     self.age=age

p1 = Person("John", 36)
print(p1.name) 
print(p1.age) 

class Person:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def mymunc(self):
        print("Hello my name is"+ self.name)
p1=Person("John",36)
p1.mymunc()
    
