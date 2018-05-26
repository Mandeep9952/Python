age = 24
print("May age is " + str(age) + " years")

print("My age is {0} years".format(age)) # other way to handle string and numeric values together

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "january", "March", "May", "July","August", "October", "December"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31))

print("My age is %d years" % age) # this is the old format of pyton2 %d replace with integer

print("My age is %d %s, %d %s" %(age, "years", 6, "months"))

for i in range(1,12):
    print("No. %2d squared is %3d,  and cubed is %4d" %(i, i ** 2, i ** 3)) # %3 give 3 space to print output, old way of Python2

print("PI is approximately %12f" % (22/7)) # %12f for giving the 12 digit space, old way of Python2

for i in range(1,12):
    print("No. {0:2} squared is {1:4},  and cubed is {2:4}" .format(i, i ** 2, i ** 3)) # giving the space to print something but new method

for i in range(1,12):
    print("No. {0:2} squared is {1:<4},  and cubed is {2:<4}" .format(i, i ** 2, i ** 3)) # if we want to align numbers from left side

print("PI is approximately {0:12.50}" .format(22/7))