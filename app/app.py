def calculate_total_and_average(marks):
    if not marks:
        return 0, 0.0
    total = sum(marks)
    average = total / len(marks)
    return total, round(average, 2)

def calculate_grade(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

def main():
    print("--- Student Grade Calculator (Push 2) ---")
    student_marks = [85, 90, 75, 80, 95]
    print(f"Processing Marks: {student_marks}")
    
    total, average = calculate_total_and_average(student_marks)
    grade = calculate_grade(average)
    
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")
    print(f"Final Grade: {grade}")

if __name__ == "__main__":
    main()
