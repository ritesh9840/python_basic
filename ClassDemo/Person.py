class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # Call the parent class constructor
        self.marks = marks


class StudentDemo:
    def __init__(self, student):
        self.student = student  # Store the Student instance

    def display_student_info(self):
        print(f"Name: {self.student.name}")
        print(f"Age: {self.student.age}")
        print(f"Marks: {self.student.marks}")


# Create a Student instance and pass it to StudentDemo
student = Student("Ram", 29, 30)
demo = StudentDemo(student)

# Display the student information
demo.display_student_info()
