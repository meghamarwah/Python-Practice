import pytest

@pytest.fixture()
def megha():
    print('This is megha block!')

def testmethod1(megha):
    print('this is test method1')

def testmethod2(megha):
    print('this is test method2')
