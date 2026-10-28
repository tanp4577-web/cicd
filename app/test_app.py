from .app import calculate_total_and_average

def test_calculate_total_and_average():
    student_marks = [85, 90, 78, 92, 80]
    total, average = calculate_total_and_average(student_marks)
    assert total == 425
    assert average == 85.0

def test_empty_marks():
    total, average = calculate_total_and_average([])
    assert total == 0
    assert average == 0.0
