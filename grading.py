student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

Student_grades = {}
for key in student_scores:

    if student_scores[key] >= 91:
        Student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        Student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        Student_grades[key] = "Acceptable"
    else:
        Student_grades[key] = "Fail"

print(Student_grades)
