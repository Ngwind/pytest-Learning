import pytest

@pytest.mark.aaa
class TestClass:

    @pytest.mark.bbb
    def test_func1(self):
        x = "this"
        assert x == "this"

    @pytest.mark.ccc
    def test_func2(self):
        x = "hello"
        assert hasattr(x, "helloqq")
