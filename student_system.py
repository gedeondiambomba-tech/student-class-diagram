class Course:
    def __init__(self, course_code: str, title: str):
        self.course_code = course_code
        self.title = title

    def __str__(self) -> str:
        return f"{self.course_code}: {self.title}"


class Student:
    def __init__(self, student_id: str, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses: list[Course] = []

    def enroll(self, course: Course) -> None:
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def list_courses(self) -> list[str]:
        return [str(course) for course in self.courses]


if __name__ == "__main__":
    student = Student("STU-101", "Maya Lin", "maya.lin@example.edu")
    course_1 = Course("CS101", "Introduction to Programming")
    course_2 = Course("SE201", "Software Modeling")

    student.enroll(course_1)
    student.enroll(course_2)
    print("Enrolled courses:", student.list_courses())