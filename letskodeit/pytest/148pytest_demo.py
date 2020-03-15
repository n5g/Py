import pytest

@pytest.fixture()
def setUp(): # можно любое другое название
    print("once before every method")

def test_methodA(setUp): # важно чтоб каждый тесть начинался со слова test
    print("Run method A")

def test_methodB(setUp):
    print("run method B")
