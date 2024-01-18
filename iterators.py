# myTuples = ("apple", "banana", "cherry")
# myTuples = "Vedas"
# myIt = iter(myTuples)
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))



# for x in myTuples:
#   print(x)


class MyNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 24:
      x = self.a
      self.a = self.a + 2
      return x
    else:
      raise StopIteration
  

myClass = MyNumber()
myIter = iter(myClass)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

for x in myIter:
  print(x)