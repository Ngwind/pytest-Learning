"""
测试fixture函数中使用yield
测试fixture参数化
"""

import pytest


@pytest.fixture()
def func1():
    print("func1")


@pytest.fixture()
def func2(func1):
    print("func2")
    return "func2"


@pytest.fixture()
def func3(func2):
    print("func3")
    return "func3"


def test_func(func2, func3):
    assert func2 == "hello"


def test_func2(func2, func3):
    assert func2 == "func1"

@pytest.fixture(params=[1,2,3])
def func4(request):
    return request.param


def test_func3(func4):
    assert 1 == func4

