class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []

  @staticmethod
  def go_to_school():
    print("I'm going to school")

  @classmethod
  def go_to_skul(cls):
    print("I'm goin' 2 skul")

cesar = Student("Cesar", "ESCOM")
Student.go_to_school()
cesar.go_to_skul()
