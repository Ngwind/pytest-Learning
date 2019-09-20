import pytest,time

def test_func1(request,pytestconfig,cache):
    print(pytestconfig.args)
    print(pytestconfig.plugins)
    # print(pytestconfig.dir)
    # print(type(pytestconfig.dir))
    # print(pytestconfig.getoption("verbose"))
    # print(pytestconfig.getini("1"))
    list = dir(request)
    for i in list:
        if not i.startswith('_'):
            print(i)
    cache.set("test/time",time.ctime())
    print(cache.get("test/time","no found"))
    print(request.fspath)
    assert 0
