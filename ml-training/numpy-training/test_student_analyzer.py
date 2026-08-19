import numpy as np
from student_analyzer import scores_mean, scores_max, scores_min, scores_median, scores_std, best_student, best_average, worst_student, worst_average, pass_student, fail_student, pass_rate, top_student, subject_mean, best_subject, grades, all_pass, level_a

def test_scores_mean():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert scores_mean(scores) == 75

def test_scores_max():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert scores_max(scores) == 90

def test_scores_min():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert scores_min(scores) == 60

def test_scores_median():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert scores_median(scores) == 75

def test_scores_std():
    scores = np.array([
        [81, 85, 87],
        [73, 75, 79]
    ])

    assert scores_std(scores) == 5   

def test_best_student():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert best_student(scores) == 1   

def test_best_average():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert best_average(scores) == 80   

def test_worst_student():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert worst_student(scores) == 2   

def test_worst_average():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert worst_average(scores) == 70

def test_pass_student():
    scores = np.array([
        [80, 90, 70],
        [60, 40, 30]
    ])

    assert pass_student(scores) == 1

def test_fail_student():
    scores = np.array([
        [80, 90, 70],
        [60, 40, 30]
    ])

    assert fail_student(scores) == 1

def test_pass_boundary():
    scores = np.array([
        [60, 60, 60],
        [59, 60, 60]
    ])

    assert pass_student(scores) == 1
    assert fail_student(scores) == 1

def test_pass_rate():
    scores = np.array([
        [80, 90, 70],
        [60, 40, 30]
    ])

    assert pass_rate(scores) == 50

def test_top1_student():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80],
        [60, 40, 30]
    ])

    assert top_student(scores, -1) == "1 - 80.00"

def test_subject_mean():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert subject_mean(scores, 0) == 70

def test_best_subject():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80]
    ])

    assert best_subject(scores) == 2

def test_grades():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80],
        [60, 40, 30]
    ])

    assert grades(scores, "B") == 1

def test_grade_boundary():
    scores = np.array([
        [60, 60, 60],   # D
        [70, 70, 70],   # C
        [80, 80, 80],   # B
        [90, 90, 90]    # A
    ])

    assert grades(scores, "D") == 1
    assert grades(scores, "C") == 1
    assert grades(scores, "B") == 1
    assert grades(scores, "A") == 1

def test_all_pass():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80],
        [60, 40, 30]
    ])

    assert all_pass(scores) == 2

def test_level_a():
    scores = np.array([
        [80, 90, 70],
        [60, 70, 80],
        [60, 40, 30]
    ])

    assert level_a(scores) == 1