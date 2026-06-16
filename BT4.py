import random
import string
from datetime import datetime




student_records = [
    {"student_id": "SV001", "name": "Nguyễn Văn A", "scores": [8.5, 7.0, 9.0]},
    {"student_id": "SV002", "name": "Trần Thị B", "scores": [4.0, 5.5, 5.0]},
    {"student_id": "SV003", "name": "Lê Văn C", "scores": [9.5, 9.0, 8.5]}
]

def calculate_average(scores):
    valid_scores = [s for s in scores if isinstance(s, (int, float))]
    if not valid_scores:
        return 0
    return sum(valid_scores) / len(valid_scores)

def classify_student(avg):
    if avg >= 8:
        return "Giỏi"
    if avg >= 6.5:
        return "Khá"
    if avg >= 5:
        return "Trung bình"
    return "Yếu"

def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for i, s in enumerate(records, 1):
        avg = calculate_average(s["scores"])
        level = classify_student(avg)
        print(f"{i}. [{s['student_id']}] {s['name']} | Điểm: {s['scores']} | ĐTB: {avg:.2f} - {level}")
    print("---------------------------------")

def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for s in records:
        s["name"] = " ".join(s["name"].strip().split()).title()
        print(f"{s['student_id']}: {s['name']}")
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")

def generate_assignment_code():
    code = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    print("--- SINH MÃ BÀI TẬP ---")
    print(f"Mã bài tập của bạn là: PY-{code}")

def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total = len(records)
    pass_count = 0
    fail_count = 0
    for s in records:
        avg = calculate_average(s["scores"])
        if avg >= 5:
            pass_count += 1
        else:
            fail_count += 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write(f"Thời gian tạo báo cáo: {now}\n")
        f.write(f"Tổng số sinh viên: {total}\n")
        f.write(f"Số sinh viên đạt yêu cầu: {pass_count}\n")
        f.write(f"Số sinh viên cần cải thiện: {fail_count}\n")
    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số sinh viên đạt yêu cầu: {pass_count}")
    print(f"Số sinh viên cần cải thiện: {fail_count}")
    print(">> Đã xuất báo cáo ra file learning_report.txt")

def main():
    while True:
        print("""
===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====
1. Xem danh sách sinh viên và điểm trung bình
2. Chuẩn hóa tên sinh viên
3. Sinh mã bài tập ngẫu nhiên
4. Xuất báo cáo học tập
5. Thoát chương trình
====================================================
""")
        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")
            continue

        match choice:
            case 1:
                display_student_scores(student_records)
            case 2:
                normalize_student_names(student_records)
            case 3:
                generate_assignment_code()
            case 4:
                export_learning_report(student_records)
            case 5:
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()