"""
测试fixture函数中使用yield

"""

import pytest

@pytest.fixture()
def fixture_func():
    print("start")
    yield
    print("end")


def test_func(fixture_func):
    assert 1
