class_hrs = {"class1":0, "class2":0, "class3":0}
# begin with inital values in your map/dictionary
study_days = int(input("How many days this week do you plan to spend studying?: "))
# create a variable asking how many days will be spent studying
class_hrs["class1"] = int(float(input("How many hours this week do you plan on studying for your first class?: ")))
class_hrs["class2"] = int(float(input("How many hours this week do you plan on studying for your second class?: ")))
class_hrs["class3"] = int(float(input("How many hours this week do you plan on studying for your third class?: ")))
# overwrite the input of the initial keys data with input from the user for each respective class, (class1, class2, class3)

# print(class_hrs)
# print(study_days) 

hour_total = sum(class_hrs.values())
# create a variable that stores the sum of the total study hours from each class
# print(hours_total)

class_avg = hour_total / study_days
# add up all the hour values and divide by the number of study days to find the daily average
# print(class_avg)

print("You should spend an average of 2.7 hours per day of studying")
# statement that shows the benchmark
print("You are spending about %.1f hours studying." % class_avg)
# statement that shows how much the user is studying based on the input

if class_avg >= 2.7:
    print("You are probably studying enough.")
else:
    print("You should probably study more each day.")
# create an if/ else statement based on whether or not the benchmark was hit or surpassed