import numpy as np
from student_analyzer import (
    scores_mean, 
    scores_max, 
    scores_min, 
    scores_median, 
    scores_std, 
    best_student, 
    best_average, 
    worst_student, 
    worst_average, 
    pass_student, 
    fail_student, 
    pass_rate, 
    top_student, 
    subject_mean, 
    best_subject, 
    grades, 
    all_pass, 
    level_a
)
students = np.genfromtxt(
    "scores.csv",
    delimiter=",",
    skip_header=1,
    dtype=np.int32
)
subject = np.genfromtxt(
    "scores.csv",
    delimiter=",",
    max_rows=1,
    dtype=str
)
print(subject)

print(students)
print("========================================")
print("        Student Score Analyzer")
print("========================================\n")
print("Students: ", students.shape[0])
print("Subjects: ", students.shape[1])
print("\n----- Overall -----")
print(f"Overall Average: {scores_mean(students):.2f}")
print(f"Overall Maximum: {scores_max(students)}")
print(f"Overall Minimum: {scores_min(students)}")
print(f"Median: {scores_median(students)}")
print(f"Standard Deviation: {scores_std(students):.2f}")
print("\n----- Students -----")
print(f"Best Student: Student {best_student(students)}")
print(f"Best Average: {best_average(students):.2f}\n")
print(f"Worst Student: Student {worst_student(students)}")
print(f"Worst Average: {worst_average(students):.2f}\n")
print(f"Pass: {pass_student(students)}")
print(f"Fail: {fail_student(students)}")
print(f"Pass Rate: {pass_rate(students):.2f}%\n")
print("\n----- Top 3 Students -----")
print(f"1. Student {top_student(students, -1)}")
print(f"2. Student {top_student(students, -2)}")
print(f"3. Student {top_student(students, -3)}")
print("\n----- Subjects -----")

for n in range(students.shape[1]):
    print(f"{subject[n].replace('_',' ').title()} Average: {subject_mean(students, n):.2f}")

print(f"\nBest Subject: Subject {best_subject(students)}")
print("\n----- Grades -----")
print(f"A: {grades(students, 'A')}")
print(f"B: {grades(students, 'B')}")
print(f"C: {grades(students, 'C')}")
print(f"D: {grades(students, 'D')}")
print(f"F: {grades(students, 'F')}")
print("\n----- Other -----")
print(f"All Subjects Passed: {all_pass(students)}")
print(f"At Least One 90+: {level_a(students)}")
print("\n========================================")
