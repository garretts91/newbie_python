a=12
b=3
print(a + b)    #15
print(a - b)    #9
print(a * b)    #36
print(a / b)    #4.0 float 
print(a // b)   #4 integer division, rounded down towards -infinity
print(a % b)    #0 modulo: the remainder after integer division
for i in range(1, a//b):
    print(i)
#You can't use float in places where an integer must be used (in the case of a/b)
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
#follows normal orders of operation
print(((a + b) /3 - 4) * 12)
#In an expression that mixes operations with equal precedence (* /, + -), they're evaluated from left to right
c = a + b 
d = c / 3
e = d - 4
print(e * 12)
print(a / (b * a) /b)