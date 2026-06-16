import math
import os
from datetime import datetime, timedelta

shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    }
]

# Tạo thư mục logs an toàn
if not os.path.exists("logs"):
    os.makedirs("logs")

print("====== HE THONG DIEU PHOI RIKKEI LOGISTICS ======")
print("Khoi tao he thong luu tru log hanh trinh... Thanh cong.")
print("-" * 70)

for s in shipments:
    # Tinh khoang cach Haversine
    R = 6371

    lat1 = math.radians(s["from_lat"])
    lon1 = math.radians(s["from_lon"])
    lat2 = math.radians(s["to_lat"])
    lon2 = math.radians(s["to_lon"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + \
        math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = R * c

    # Tinh ETA
    depart_time = datetime.strptime(s["depart"], "%Y-%m-%d %H:%M:%S")
    hours_needed = distance_km / 60
    eta = depart_time + timedelta(hours=hours_needed)

    deadline = datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")

    if eta <= deadline:
        status = "AN TOAN (Kip tien do)"
    else:
        status = "CANH BAO (Tre han)"

    print(f"CHUYEN XE {s['id']}")
    print(f"  Khoang cach van chuyen: {distance_km:.2f} km")
    print(f"  Thoi gian khoi hanh: {depart_time}")
    print(f"  Du kien cap ben (ETA): {eta}")
    print(f"  Trang thai: {status}")
    print("-" * 70)