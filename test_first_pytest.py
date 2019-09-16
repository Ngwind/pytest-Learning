# 被测试函数
def func(x):
    return x+1

def test_func():
    assert 3 == func(1), "func函数测试不通过"

test_func()