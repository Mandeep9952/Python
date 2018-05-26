greeting = "Bruce"
_myName = "mandeep"
Tim_ws_45 = "kgjigj"
Tim45 = "jhjh"
Greeting = "lkjhjfh "

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b) # that's for division but if we want result in whole number

for i in range(1, 4):
    print(i)
for i in range(1, a//b): # wrong if we divide integer with float number
    print(i)

print(a + b / 3 - 4 * 12) # answer is wrong because python follows the BODMAS

print((((a+b) / 3)-4) *12) # solutions is arrange the breakets

#other way to solve store in different varibles

c = a+b
d = c/3
e = d-4
print(e*12)