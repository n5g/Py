import pytest

@pytest.yield_fixture()
def setUp(): # можно любое другое название
    print("once before every method") #эта строка будет выполнятся перед каждым методом
    yield #разделяет каждый тест на до и после
    print("once after every method") #эта строка будет выполнятся после каждого метода

def test_methodA(setUp): # важно чтоб каждый тесть начинался со слова test
    print("Run method A")

def test_methodB(setUp):
    print("run method B")
