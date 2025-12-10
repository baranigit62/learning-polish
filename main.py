
def main():
    print("Hello from learning-polish!")
a = 2
b = 4
def calculator(a,b):
    print(a + b)

print("baran")
main()
calculator(a,b)
elements = ["apple" , "ananas", "orange"]
for element in elements:
    print(element)
    

student = {
    "index number" : "35431",
    "name" : "baran",
    "school": "wseiz",
    "age": 20
}

calculator(student["age"], 10)
class Animal:
   def __init__(self,age,name):
       self.name = name
       self.age = age
p1 = Animal(20,"baran")
print(p1.age)
print(p1.name)