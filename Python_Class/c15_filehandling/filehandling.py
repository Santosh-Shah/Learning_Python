# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


# import os
# print(os.getcwd())


# f = open("Python.pdf", "r")
# f = open("C:\pythonClass\c15_filehandling\hello.txt", "r")
# f = open("C:\pythonClass\c15_filehandling\hello.txt", "a")

# f = open("C:\pythonClass\c15_filehandling\hello.txt", "w")


# f = open("C:\pythonClass\c15_filehandling\Python.pdf", "r")

# print(f.read(10))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f.write("I want to be a software developer")
# f.close()

# f = open("C:\pythonClass\c15_filehandling\hello.txt", "r")

# print(f.read())

# for x in f:
#   print(x)







# creating new file
# f = open("name.txt", "x")
# f.close()

# writing in new file
# f = open("name.txt", "w")
# # f.close()

# f.write("Hello everyone my name is Santosh Shah")
# f.close()

# f = open("name.txt", "rt")

# print(f.read())


import os
# os.remove("name.txt")

if os.path.exists("name.txt"):
  os.remove("name.txt")
else:
  print("The file name.txt not exits")

# deleting folder
os.rmdir("helo")