import math
import os
from datetime import datetime, timedelta

# Du lieu ban dau
flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

# ================== HELPER FUNCTIONS ==================

def check_duplicate_id(flight_id, flight_list):
    flight_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"] == flight_id:
            return True
    return False


def show_flights_and_logistics():
    print("----- DANH SACH CHUYEN BAY & HAU CAN -----")
    for index, flight in enumerate(flights, start=1):
        water_boxes = math.ceil(flight["passengers"] / 10)
        print(
            f"{index}. Ma: {flight['flight_id']} | "
            f"Khoi hanh: {flight['depart_time']} | "
            f"So khach: {flight['passengers']} | "
            f"Du phong: {water_boxes} thung nuoc."
        )


def add_new_flight():
    print("----- TIEP NHAN CHUYEN BAY MOI -----")

    flight_id = input("Nhap ma chuyen bay: ").strip().upper()

    if check_duplicate_id(flight_id, flights):
        print("Loi: Ma chuyen bay da ton tai.")
        return

    try:
        passengers = int(input("Nhap so luong hanh khach: "))
        depart_time = input("Nhap thoi gian cat canh (YYYY-MM-DD HH:MM:SS): ")
        datetime.strptime(depart_time, "%Y-%m-%d %H:%M:%S")
        duration_min = int(input("Nhap so phut bay: "))
    except ValueError:
        print("Sai dinh dang thoi gian! Vui long nhap dung YYYY-MM-DD HH:MM:SS")
        return

    flights.append({
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time,
        "duration_min": duration_min
    })

    print(f">> Them chuyen bay {flight_id} thanh cong!")


def calculate_eta():
    print("----- TINH TOAN THOI GIAN HA CANH (ETA) -----")
    flight_id = input("Nhap ma chuyen bay can tinh: ").strip().upper()

    for flight in flights:
        if flight["flight_id"] == flight_id:
            depart_time = datetime.strptime(flight["depart_time"], "%Y-%m-%d %H:%M:%S")
            eta = depart_time + timedelta(minutes=flight["duration_min"])

            print(f"-> Chuyen bay {flight_id} cat canh luc: {depart_time}")
            print(f"-> Thoi gian ha canh du kien (ETA): {eta}")
            return

    print("Khong tim thay chuyen bay.")


def create_log_directory():
    print("----- KHOI TAO THU MUC HE THONG -----")
    folder_name = "aviation_logs"

    if not os.path.exists(folder_name):
        print(f"[SYSTEM] Thu muc '{folder_name}' chua ton tai. Dang khoi tao...")
        os.mkdir(folder_name)
        print("[SYSTEM] Tao thu muc thanh cong!")
    else:
        print("Thu muc da ton tai, bo qua buoc khoi tao.")

# ================== MAIN MENU ==================

def show_menu():
    print("\n===== HE THONG DIEU HANH BAY RIKKEI AVIATION =====")
    print("1. Hien thi lich trinh va thong ke hau can")
    print("2. Tiep nhan chuyen bay moi")
    print("3. Tinh thoi gian ha canh du kien (ETA)")
    print("4. Khoi tao thu muc luu tru log he thong")
    print("5. Thoat chuong trinh")
    print("================================================")


while True:
    show_menu()
    try:
        choice = input("Nhap lua chon cua ban: ")
    except ValueError:
        print("Lua chon khong hop le. Vui long nhap so tu 1 den 5.")
        continue
    match choice:
        case "1":
            show_flights_and_logistics()
        case "2":
            add_new_flight()
        case "3":
            calculate_eta()
        case "4":
            create_log_directory()
        case "5":
            print("Cam on ky su da su dung he thong!")
            break
        case _:
            print("Lua chon khong hop le. Vui long nhap tu 1 den 5.")