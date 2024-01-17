class MyClass:
  x = 15
  y = 200

# print(MyClass)
# print(MyClass.x)
yValue = MyClass()
print(yValue.y)


# using __init__ function and 
# using __str__ function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Raj", 55)
print(p1.name, p1.age)
print(p1)




#--------------
# class Person2:
#   def __init__(self, name1, name2, age):
#     self.name1 = name1
#     self.name2 = name2
#     self.age = age
  
#   def myFunc(self):
#     print("This is init function: " + self.name1)

# xxx = Person2("Ram", "Shyam", 63)
# xxx.myFunc()



# class Person2:
#   def __init__(hello, name1, name2, age):
#     hello.name1 = name1
#     hello.name2 = name2
#     hello.age = age
  
#   def myFunc(pagal):
#     print("This is init function: " + pagal.name2)

# xxx = Person2("Ram", "Shyam", 63)

# # updating object's attibute
# xxx.name2 = "Shyam Shundar"

# # # deleting 
# # del xxx.name2

# del xxx

# xxx.myFunc()


class Person3:
  pass

