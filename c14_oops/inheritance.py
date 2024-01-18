class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printName(self):
    print(self.fname, self.lname)

# class Student(Person):
#     pass
    
class Student(Person):
  hell = "Flow"
  def __init__(self, fname, lname, year):
    # Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.role = "Software Developer"
    self.graduationYear = year

  def welcom(self):
    print("welcome", self.fname, self.lname, "to the class of ", self.graduationYear)
x = Student("Mike", "Orra", 2025)
x.printName()
x.welcom()
print(x.role, x.graduationYear)
# print(x.hell)