#check stackoverflow "how to clone or copy a list"
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)


digits = list("23984238974871326478932")
digits_ordered = sorted(digits)
print(digits)
print(digits_ordered)

#more_numbers = list(numbers)
#more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)

print(numbers is more_numbers)
print(numbers == more_numbers)


# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)

# even.sort(reverse=True)
# print(even)
# print(another_even)