#!/usr/bin/env python3
# -*- coding: utf-8 -*-  # noqa: UP009
"""
Developer: Miguel Jara Maldonado.
Creation Date: 2026-11-09.
Description: Working code that fails to use the best practices.
"""


def summarize_grades(grades: list):
    total = 0
    highest = None
    for grade in grades:
        if type(grade) == str:
            grade = float(grade)
        total += grade
        if highest is None or grade > highest:
            highest = grade
    average = total / len(grades)
    return f"Average: {average} / Max: {highest}"


def print_approved(students: list):
    for student in students:
        try:
            age = int(student["age"])
        except ValueError:
            age = 0
        if student["status"] == "approved":
            print(student["name"], age)


if __name__ == "__main__":
    students = [
        {"name": "Ana", "age": "20", "status": "approved"},
        {"name": "Luis", "age": "unknown", "status": "failed"},
    ]
    print(summarize_grades([7.5, 8, 9]))
    print_approved(students)
