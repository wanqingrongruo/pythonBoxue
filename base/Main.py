
from Person import Person
from Employee import Employee


roni = Employee(1, "ronizheng", 25)
print(issubclass(Employee, Person))
print(isinstance(roni, Person))  
print(isinstance(roni, Employee))

print(roni.__repr__())  # 类型表达
print(roni.__str__())


mars = Employee(1, "ronizheng", 25)
print(mars == roni)
print(Employee._Employee__counter)
