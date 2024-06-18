
"""s = " "
for i in range(100):
    s = s + str(i)
"""
# print(s)

#the code above is highly inefficient since 
# a new copy of the string has to be created each time

return_string = ", ".join(str(i) for i in range(100))

print(return_string)