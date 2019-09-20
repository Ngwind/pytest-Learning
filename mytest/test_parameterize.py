"""
实验参数化装饰器的参数格式
"""
import pytest


class Obs(object):
    def __init__(self, n1=0, n2=0, n3=0):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def __str__(self):
        return "obs:{},{},{}".format(self.n1, self.n2, self.n3)


def obs_to_str(obs):
    return 'obs:{},{},{}'.format(obs.n1, obs.n2, obs.n3)


obs_list = [Obs(1, 1, 1), Obs(1, 2, 2), Obs(-1, 1, 1)]


class Testclass(object):
    @pytest.mark.parametrize("obs", obs_list, ids=obs_to_str)
    def test_para(self, obs):
        if obs.n2 == 2:
            print("haha")
        assert obs.n1 == 1 and obs.n2 == 2 or obs.n3 == 3
