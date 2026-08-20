class Student:
    school_name = "S N KANSAGRA School"

    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        self.marks = []

    def add_mark(self, score):
        self.marks.append(score)

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Grade:", self.grade)
        print("School:", Student.school_name)
        print("Average Marks:", round(self.calculate_average(), 2))
        print("-" * 30)

# Creating student objects
student1 = Student("Rahul", 6, "10th")
student2 = Student("Kartik", 22, "10th")

# Adding marks
student1.add_mark(85)
student1.add_mark(90)
student1.add_mark(78)

student2.add_mark(92)
student2.add_mark(88)
student2.add_mark(95)

# Displaying student details
print("--- Student Details ---")

student1.display_info()
student2.display_info()