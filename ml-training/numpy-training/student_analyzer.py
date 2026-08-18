import numpy as np

def main():
    scores = np.random.randint(0, 101, size=(30, 5))
    print(scores)
    print("========================================")
    print("        Student Score Analyzer")
    print("========================================\n")
    students = scores.shape[0]
    subjects = scores.shape[1]  
    print("Students: ", students)
    print("Subjects: ", subjects)
    print("\n----- Overall -----")
    print(f"Average 平均: {scores_mean(scores):.2f}")
    print(f"Maximum 最高分: {scores_max(scores)}")
    print(f"Minimum 最低分: {scores_min(scores)}")
    print(f"Median 中位數: {scores_median(scores):.2f}")
    print(f"Std 標準差: {scores_std(scores):.2f}")
    print("\n----- Students -----")
    print(f"Best Student: Student {best_student(scores)}")
    print(f"Best Average: {best_average(scores):.2f}\n")
    print(f"Worst Student: Student {worst_student(scores)}")
    print(f"Worst Average: {worst_average(scores):.2f}\n")
    print(f"Pass: {pass_student(scores)}")
    print(f"Fail: {fail_student(scores)}")
    print(f"Pass Rate: {pass_rate(scores):.2f}%\n")
    print("\n----- Top 3 Students -----")
    print(f"1. Student {top_student(scores, -1)}")
    print(f"2. Student {top_student(scores, -2)}")
    print(f"3. Student {top_student(scores, -3)}")
    print("\n----- Subjects -----")
    print(f"Subject 1 Average: {subject_mean(scores, 0):.2f}")
    print(f"Subject 2 Average: {subject_mean(scores, 1):.2f}")
    print(f"Subject 3 Average: {subject_mean(scores, 2):.2f}")
    print(f"Subject 4 Average: {subject_mean(scores, 3):.2f}")
    print(f"Subject 5 Average: {subject_mean(scores, 4):.2f}")
    print(f"\nBest Subject: Subject {best_subject(scores)}")
    print("\n----- Grades -----")
    print(f"A: {grades(scores, 'A')}")
    print(f"B: {grades(scores, 'B')}")
    print(f"C: {grades(scores, 'C')}")
    print(f"D: {grades(scores, 'D')}")
    print(f"F: {grades(scores, 'F')}")
    print("\n----- Other -----")
    print(f"All Subjects Passed: {all_pass(scores)}")
    print(f"At Least One 90+: {level_a(scores)}")
    print("\n========================================")

def scores_mean(s):
    return np.mean(s)

def scores_max(s):
    return np.max(s)

def scores_min(s):
    return np.min(s)

def scores_median(s):
    return np.median(s)

def scores_std(s):
    return np.std(s)

def best_student(s):
    return np.argmax(np.mean(s, axis=1))+1

def best_average(s):
    return np.max(np.mean(s, axis=1))

def worst_student(s):
    return np.argmin(np.mean(s, axis=1))+1

def worst_average(s):
    return np.min(np.mean(s, axis=1))

def pass_student(s):
    student_mean = np.mean(s, axis=1)
    return np.sum(student_mean >= 60)

def fail_student(s):
    student_mean = np.mean(s, axis=1)
    return np.sum(student_mean < 60)
   
def pass_rate(s):
    student_mean = np.mean(s, axis=1)
    return np.mean(student_mean >= 60) * 100

def top_student(s, n):
    student_mean = np.mean(s, axis=1)
    ranking = np.argsort(student_mean)
    index = ranking[n]
    return f"{index + 1} - {student_mean[index]:.2f}"

def subject_mean(s, n):
    return np.mean(s, axis=0)[n]

def best_subject(s):
    return np.argmax(np.mean(s, axis=0))+1

def grades(s, g):
    student_mean = np.mean(s, axis=1)
    conditions = [
        student_mean < 60,
        student_mean < 70,
        student_mean < 80,
        student_mean < 90
    ]
    choices = [
        "F",
        "D",
        "C",
        "B"
    ]
    result = np.select(conditions, choices, default="A")
    # return np.count_nonzero(result == g)
    return np.sum(result == g)

def all_pass(s):
    return np.count_nonzero(np.all(s >= 60, axis=1))

def level_a(s):
    return np.count_nonzero(np.any(s >= 90, axis=1))

if __name__ == "__main__":
    main()
