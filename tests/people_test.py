from src.objects.people import boy

def test_boy():
    person = boy(15)
    assert person.get_age() == 15