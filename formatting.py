for i in range(1, 13):
    print("{0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))    #{Field:FieldWidth}

print()

for i in range(1, 13):
    print("{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))    #{Field:FieldWidth}   Left Alignment

#Field Width Alginment: < Left Alignment ^ Center Alignment

print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))