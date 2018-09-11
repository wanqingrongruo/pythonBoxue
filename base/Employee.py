
from Person import Person


class Employee(Person):
    __counter = 0  # 所有类对象共享
    def __init__(self, work_id, name, age):
        Person.__init__(self, name, age)
        self.work_id = work_id
        Employee.__counter += 1
    

    def __str__(self):
        return "Employee"
    
    def __eq__(self, other):
        return self.work_id == other.work_id and self.name == other.name and self.age == other.age
