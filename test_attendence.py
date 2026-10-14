from attendance import check_attendance

def test_eligible():
    assert check_attendance(40, 50) == (80.0, "Eligible")

def test_not_eligible():
    assert check_attendance(30, 50) == (60.0, "Not Eligible")

def test_boundary():
    assert check_attendance(3, 4) == (75.0, "Eligible")
