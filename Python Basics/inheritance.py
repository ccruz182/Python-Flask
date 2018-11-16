class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []

  @classmethod
  def friend(cls, origin, friend_name, salary):
    return cls(friend_name, origin.school, salary)

"""
anna = Student("Anna", "Oxford")
friend = anna.friend("Greg")
print(friend.name)
"""

class WorkingStudent(Student):
  def __init__(self, name, school, salary):
    super().__init__(name, school)
    self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 6000)
print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 1000)
print(friend.name)
print(friend.salary)
