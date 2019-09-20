import time

def test_needfiles(tmpdir):
    print(tmpdir)
    tmpdir.join("test.txt").write(time.ctime())
    assert 0
