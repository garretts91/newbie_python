import numbers


greeting = "Good "
greeting += "Morning "
print(greeting)

greeting *= 5
print(greeting)

#Check python docs -> Operator Precedence

number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer += number

print(answer)