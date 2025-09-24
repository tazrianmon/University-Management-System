# ---------- University Management System (Module 7) ----------

class Person:
    """Base class: tracks total people via a class variable."""
    total_people = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.total_people += 1

    def introduce(self) -> str:
        return f"Hi, I am {self.name}, {self.age} years old."

    @classmethod
    def get_total_people(cls) -> str:
        return f"Total people: {cls.total_people}"


class Student(Person):
    """Student extends Person; encapsulates GPA with property."""
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list: list[str] = []
        self.__gpa: float = 0.0   # private

    # behavior
    def enroll_course(self, course: str) -> None:
        self.course_list.append(course)

    def show_courses(self) -> str:
        return (
            f"{self.name}'s Courses: {', '.join(self.course_list)}"
            if self.course_list else f"{self.name} has no courses yet."
        )

    # encapsulation: GPA property with validation
    @property
    def gpa(self) -> float:
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float) -> None:
        if 0.0 <= value <= 4.0:
            self.__gpa = float(value)
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # static utility
    @staticmethod
    def is_valid_id(student_id: str) -> bool:
        return student_id.startswith("S-")


class Teacher(Person):
    """Teacher extends Person; overrides introduce()."""
    def __init__(self, name: str, age: int, employee_id: str, subject: str):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def introduce(self) -> str:
        return f"I am Professor {self.name}, teaching {self.subject}."


def display_role(person: Person) -> str:
    """Polymorphism: behaves differently by runtime type."""
    if isinstance(person, Student):
        return f"{person.name} is a Student (ID: {person.student_id})."
    if isinstance(person, Teacher):
        return f"{person.name} is a Teacher (Subject: {person.subject})."
    return f"{person.name} is a Person."


class GraduateStudent(Student):
    """Inheritance type: Student -> GraduateStudent adds thesis_title."""
    def __init__(self, name: str, age: int, student_id: str, thesis_title: str):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    def show_thesis(self) -> str:
        return f"Graduate Student {self.name}'s Thesis: {self.thesis_title}"


# ----------------- Demo / Quick Test -----------------
if __name__ == "__main__":
    # Students
    s1 = Student("Alice", 20, "S-101")
    s1.enroll_course("Math")
    s1.enroll_course("Physics")
    s1.gpa = 3.8

    # Teacher
    t1 = Teacher("Dr. Smith", 45, "T-500", "Computer Science")

    # Graduate student
    g1 = GraduateStudent("Bob", 24, "S-201", "AI in Healthcare")
    g1.gpa = 3.6

    # Outputs
    print(s1.introduce())
    print(s1.show_courses())
    print("Valid ID?", Student.is_valid_id(s1.student_id))
    print("Alice GPA:", s1.gpa)

    print(t1.introduce())
    print(display_role(t1))

    print(g1.introduce())
    print(g1.show_thesis())

    print(Person.get_total_people())
