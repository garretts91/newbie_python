shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_shopping_list = shopping_list
print(id(shopping_list))
print(id(another_shopping_list))

#augmented assignment (concatenation)

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_shopping_list)
#id remains unchanged because it is mutable and does not need to create a new list
a = b = c = d = e = f = another_shopping_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)

#python docs - mutable sequence types - common sequence operations

