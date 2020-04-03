from src.objects.shape import square, cube
from tests.unit_tests import test_square, test_cube

a = square(5)
b = cube(10)
print(a.area())
b.who_am_i()

test_square()
test_cube()
