import pytest
# 使用pytest -m 'smoke'执行测试时，只会运行test_func1()
@pytest.mark.smoker
def test_func1():
    assert 1==0

def test_func2(): 
    assert 1==2
