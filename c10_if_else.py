# a = 4500
# b = 450
# if a > b:
#     print("a is greater")
# elif a == b:
#     print("both are equal")
# else:
#     print("b is greater")


# shorthand for above condition
# if a > b: print("a is greater")

# This technique is known as Ternary Operators, or Conditional Expressions.
# print("a is greater") if a > b else print("b is greater")

# print("a is greater") if a > b else print("both are equals") if a == b else print("b is greater")


# And, or & not operators
# a = 5
# b = 45
# c = 50
#
# if a < b and c > a:
#     print("yes! you are right")
#
# if c > b or c < b:
#     print("Yes! you are also right")
#
# if a != c:
#     print("Yes, Of course! you are right too")





# nested if statements
x = 21
if x > 18:
    print("Yes!, x > 18")
    if x > 20:
        print("Yes! x is greater than 20")
    else:
        print("Not!, x is just", x)



# Pass statement to avoid error
a = 500
b = 60

if a > b:
    pass

