"""
通过@pytestmark.usefixtures()来给函数指定fixtures
"""

import pytest


@pytest.fixture()
def fix_func1():
    print("setup1")
    yield
    print("teardown1")


@pytest.fixture()
def fix_func2():
    print("setup2")
    yield
    print("teardown2")


@pytest.mark.usefixtures("fix_func1", "fix_func2")
class TestClass1():

    def test_func1(self):
        assert 1

    def test_func2(self):
        assert 1 == 1
