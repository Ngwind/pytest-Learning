"""
试验fixture()的autouse参数
"""
import pytest


@pytest.fixture(autouse=True)
def fix_func1():
    return 1


def test_func1():
    assert 1 == fix_func1  # fix_func1 == <function fix_func1 at 0x0000024E5272C378>
