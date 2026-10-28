def calculate_total_and_average(marks):
    if not marks:
        return 0, 0.0
    total = sum(marks)
    average = total / len(marks)
    return total, round(average, 2)

def main():
    print("--- Student Grade Calculator (Push 1) ---")
    student_marks = [85, 90, 78, 92, 80]
    print(f"Processing Marks: {student_marks}")
    
    total, average = calculate_total_and_average(student_marks)
    
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")

if __name__ == "__main__":
    main()
