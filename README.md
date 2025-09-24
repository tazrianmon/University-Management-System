# University-Management-System

A Python-based **University Management System** showcasing core OOP concepts: inheritance, polymorphism, encapsulation, class variables/methods, and static methods. Built for Module 7 assignment.

## Features
- **Person (Base)**: `name`, `age`, `introduce()`, class counter + `get_total_people()`
- **Student (Person)**: `student_id`, `course_list`, `enroll_course()`, `show_courses()`
  - Encapsulation: private `__gpa` + property setter/getter (0.0–4.0)
  - Static method: `is_valid_id("S-...")`
- **Teacher (Person)**: `employee_id`, `subject`, overrides `introduce()`
- **GraduateStudent (Student)**: adds `thesis_title`
- **Polymorphism**: `display_role(person)` behaves per type

## How to Run
```bash
python university.py
