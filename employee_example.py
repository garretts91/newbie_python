#Employee example

class Employee:
#Common base class for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.empNum = Employee.empCount

    def displayCount(self):
        print ("%s is employee %d of %d" % (self.name,self.empNum,Employee.empCount))

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)

#This would create first object of Employee class
Luke = Employee("Luke", 2000)
#This would create second object of Employee class
Han = Employee("Han", 3000)

Luke.displayEmployee()
Han.displayEmployee()
Luke.displayCount()
Han.displayCount()

#Manager class derived from Employee that also has a department and can adjust salaries
class Manager(Employee):

    def __init__(self, name, salary, department):
        self.department = department
        Employee.__init__(self, name, salary)

    def displayManager(self):
        self.displayEmployee()
        print("%s manages the %s department." % (self.name, self.department))

    def adjustSalary(self, employee, amount, reason):
        employee.salary += amount
        print ("%s\'s new salary is %s." % (employee.name,employee.salary))
        print ("Reason for adjustment: %s" % reason)

class SithLord(Employee):
    
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def light_saber(self, hilt, color):
        self.hilt = hilt
        self.color = color
        print("%s\'s lightsaber hilt is %s and is %s." % (self.name, self.hilt, self.color))

    def force_powers(self, power):
        self.power = power
        print("%s is a notorious user of %s" % (self.name, self.power))

Palpatine = SithLord("Emperor Palpatine", 10000)

print(Palpatine.light_saber("Avenger", "Red"))
print(Palpatine.force_powers("Force Lightning"))

Palpatine.displayEmployee()
Palpatine.displayCount()

Darth=Manager("Darth Vader",4500,"Death Star")

Darth.displayManager()

#Only Managers can adjust salaries
Darth.adjustSalary(Luke,-23,"Attacking my department")