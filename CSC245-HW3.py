#OOP in Python

class Student:
    #Initializing members
    def __init__(self, name, student_id, gpa):
        self.__name=name
        self.__student_id=student_id
        self.__gpa=gpa
        self.__attendance=0

    #Implementing methods
    def mark_attendance(self):
        self.__attendance+=1
    def get_attendance(self):
        return self.__attendance

    #Implementing setter and getter methods to retrieve information
    def get_name(self):
        return self.__name
    def get_student_id(self):
        return self.__student_id
    def get_gpa(self):
        return self.__gpa

    def set_name(self, name):
        self.__name=name
    def set_student_id(self, student_id):
        self.__student_id=student_id
    def set_gpa(self, gpa):
        self.__gpa=gpa
    #Displaying student info
    def display_info(self):
        print(f"Student name: {self.__name}")
        print(f"Student ID: {self.__student_id}")
        print(f"GPA: {self.__gpa}")
        print(f"Attendance: {self.__attendance}\n")

class Course:
    #Initializing members
    def __init__(self, course_name):
        self.course_name=course_name
        self.students=[]

    #Implementing methods
    def add_student(self, student):
        self.students.append(student)

    #Removing student by id
    def remove_student(self, student_id):
        for student in self.students:
            if student_id == student.get_student_id():
                self.students.remove(student)
                print(f"Removed student {student.get_name()}")
                return
        raise ValueError(f"Student with ID {student_id} not found.")

    #Displaying student info by course
    def display_info(self):
        print(f"Students enrolled in {self.course_name}\n")
        if not self.students:
            print("No students enrolled in this course.")
        else:
            for student in self.students:
                student.display_info()

#Example Usage
student1=Student("Angelina", "12345", 3.9)
student2=Student("Matt", "56789", 3.8)
student3=Student("Kon", "99999", 3.6)

course=Course("CSC 245")

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

student1.mark_attendance()
student2.mark_attendance()
student3.mark_attendance()

course.display_info()

