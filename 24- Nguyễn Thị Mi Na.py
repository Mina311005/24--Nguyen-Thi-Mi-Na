student_list = []
 
def add_student(name, year_of_birth, address):
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")


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


def main():
    while True:
        print("\n=== QUAN LY SINH VIEN ===")
        print("1. Them sinh vien")
        print("2. Xem danh sach")
        print("3. Tim kiem sinh vien")
        print("0. Thoat")

        choice = input("Chon chuc nang: ").strip()

        if choice == "1":
            name = input("Nhap ten: ").strip()
            year = input("Nhap nam sinh: ").strip()
            address = input("Nhap dia chi: ").strip()
            add_student(name, year, address)
        elif choice == "2":
            print_student_list()
        elif choice == "3":
            key = input("Nhap ten can tim: ").strip()
            search_student(key)
        elif choice == "0":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Thu lai.")


if __name__ == "__main__":
    main()

