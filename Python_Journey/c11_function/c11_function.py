# def helloFuntion():
#   print("Hello Function")


# helloFuntion()


# paramitrized function
# def nameFuntion(name):
#   print(name + " is my name")


# nameFuntion("Manish Babuwa")
# nameFuntion("Rohit SHah")
# nameFuntion("Hariom Shah")

# print("Hello")



# def twoArg(arg1, arg2):
#   print(arg1 + " " + arg2)

# must have to pass two arguments, otherwise throw error
# twoArg("Ram", "Hari")

#interger in not working till now
# twoArg(25, 30)


# let's have the list of arguments 
def tuplesFuntion(*names):
  print("Boys names: " + names[2])

tuplesFuntion("Ram", "Shywam", "Hari", "Rabi")


#keyword arguments
# def keyFunctons(key1, key2, key3):
#   print("All keyword: " + key1 + ", " + key2)

# keyFunctons(key1 = "Hariom", key2 = "Rohit", key3 = "Santosh")


# use if you don't know how many keyword you have passed or have to pass
#keyword arguments
def keyFunctons(**key):
  print("All keyword: " + key["key1"])

keyFunctons(key1 = "Hariom", key2 = "Rohit", key3 = "Santosh")


# using default parameter value
def defaultFuntion(collegeNam = "Vedas College"):
  print("i college name is: " + collegeNam)

defaultFuntion()
defaultFuntion("DAV")



# passing a lists of arguments
def listFunction(food):
  for x in food:
    print(x)

fruits = ["Apple", "Banana", "Coconuts"]
listFunction(fruits)



# function that return values
def returnFunction(value):
  return value + 10

print(returnFunction(10))
print(returnFunction(15))
print(returnFunction(20))



# pass statement are used if you just want be safe from error
def helloName():
  pass


# using positonal arguments
def positonalFunction(value, /):
  print(value)

  # Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

positonalFunction(522)



# Keyword-Only Arguments
def keywordOnlyFun(*, value):
  print(value)

keywordOnlyFun(value = "It will have only keyword argument")



# Combine Positional-Only and Keyword-Only
def posAndKeyFun(a, b, /, *, c, d):
    print("a:", a, " b:", b, " c:", c, " d:", d)

posAndKeyFun(50, 70, c="Punam", d="Pandey")