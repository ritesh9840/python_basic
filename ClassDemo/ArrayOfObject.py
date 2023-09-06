from ClassDemo.Person import Student

students = [
    Student("Ram", 20, 30),
    Student("Mohan", 21, 30),
    Student("Shyam", 20, 30)
]

total_age = sum(student.age for student in students)
num_students = len(students)

if num_students > 0:
    average_age = total_age / num_students
    print(f"Average age of students: {average_age}")

