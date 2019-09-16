class TestClass:

    def test_func1(self):
        x = "this"
        assert x == "this"

    def test_func2(self):
        x = "hello"
        assert hasattr(x, "helloqq")
