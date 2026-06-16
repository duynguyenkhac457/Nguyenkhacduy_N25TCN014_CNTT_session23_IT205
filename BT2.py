import os
import math
from datetime import datetime

raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

# Tao thu muc luu tru an toan
os.makedirs("media_vault", exist_ok=True)

print("===== HE THONG XU LY MEDIA FILE =====")
print("-" * 60)

for file in raw_files:
    # 1. Tinh so block o dia (4096 bytes / block)
    blocks = math.ceil(file["size_bytes"] / 4096)

    # 2. Xu ly ngay upload an toan
    try:
        upload_date = datetime.strptime(file["upload_at"], "%Y-%m-%d")
        date_status = "HOP LE"
    except ValueError:
        upload_date = None
        date_status = "SAI DINH DANG NGAY"

    # 3. In thong tin
    print(f"Ten file: {file['filename']}")
    print(f"  Kich thuoc: {file['size_bytes']} bytes")
    print(f"  So block chiem dung: {blocks}")
    print(f"  Ngay upload: {file['upload_at']} ({date_status})")
    print("-" * 60)