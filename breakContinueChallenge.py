# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)