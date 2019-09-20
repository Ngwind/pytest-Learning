"""
试验pytest.fixture函数的ids参数
"""
import pytest


class A(object):
    """
    参数化数据类
    """

    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3


a_list = [A(1, 1, 1), A(2, 2, 2), A(3, 3, 3)]  # 保存参数化数据的列表


def a_to_str(a):
    """
    将A对象转化为字符串的函数
    """
    return "A({},{},{})".format(a.n1, a.n2, a.n3)


@pytest.fixture(name="fix", autouse=True, scope="function", params=a_list, ids=a_to_str)
def fix_func(request):
    """fixture函数,作用域为函数域，默认使用此fixture,重命名为fix,参数化3组对象，返回每一组参数化数据对象,自定义每组参数化数据的id"""
    return request.param


@pytest.mark.parametrize("a,b,c", [("a","a","a"),("b","b","b")])
def test_func(fix,a,b,c):
    """
    测试用例函数
    """
    print(a,b,c)
    assert fix.n1 == 1 and fix.n2 == 1 and fix.n3 == 1
