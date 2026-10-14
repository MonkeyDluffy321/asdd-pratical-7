def check_attendance(attended, total):
    if total <= 0 or attended < 0 or attended > total:
        raise ValueError("Invalid attendance")

    per = round(attended / total * 100, 2)
    status = "Eligible" if per >= 75 else "Not Eligible"
    return per, status

if __name__ == "__main__":
    per, status = check_attendance(42, 50)
    print(f"Attendance: {per}%")
    print(f"Status: {status}")
