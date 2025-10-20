def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")
