def search_student(search_name):
    print("--- KET QUA TIM KIEM ---")
    results = []
    for student in student_list:
        if search_name.lower() in student['name'].lower():
            results.append(student)

    if results:
        for s in results:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
    else:
        print("Khong tim thay sinh vien nao.")
