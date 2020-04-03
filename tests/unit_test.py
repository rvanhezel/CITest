from src.objects.shape import square, cube

def test_square():
    a = square(5)
    assert a.area() == 25

def test_cube():
    a = cube(5)
    assert a.area() == 120