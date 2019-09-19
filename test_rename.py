"""
试验fixtrue的重命名
"""
import pytest


@pytest.fixture(name="new_fix_func")
def fix_func():
    return 1


def test_func(new_fix_func):
    assert new_fix_func == 1
