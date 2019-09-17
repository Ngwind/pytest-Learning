"""
实验参数化装饰器的参数格式
"""
import pytest

class Testclass(object):
    
    @pytest.mark.parametrize("n1,n2,n3", [(-1,1,1),(1,2,2),(1,2,"3")])
    def test_para(self, n1, n2, n3):
        if n2 == 2:
            print("haha")
        assert n1 == 1 and n2 == 2 or n3 ==3
