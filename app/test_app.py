from .app import calculate_total_and_average, calculate_grade

def test_calculate_total_and_average():
    student_marks = [85, 90, 75, 80, 95]
    total, average = calculate_total_and_average(student_marks)
    assert total == 425
    assert average == 85.0

def test_calculate_grade():
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(72) == 'C'
    assert calculate_grade(64) == 'D'
    assert calculate_grade(45) == 'F'

def test_empty_marks():
    total, average = calculate_total_and_average([])
    assert total == 0
    assert average == 0.0
