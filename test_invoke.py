"""
测试使用python -m调用和使用pytest调用时，sys.path的区别
"""
import sys


def test_path():
    print(sys.path)
    assert 0

a = ['E:\\pytestLearning\\pytest-Learning', 'D:\\python\\Scripts\\pytest.exe', 'd:\\python\\python37.zip', 'd:\\python\\DLLs', 'd:\\python\\lib', 'd:\\python', 'C:\\Users\\wuwenda\\AppData\\Roaming\\Python\\Python37\\site-packages', 'd:\\python\\lib\\site-packages', 'd:\\python\\lib\\site-packages\\win32', 'd:\\python\\lib\\site-packages\\win32\\lib', 'd:\\python\\lib\\site-packages\\Pythonwin']
a.sort()
b = ['E:\\pytestLearning\\pytest-Learning', 'D:\\python\\python37.zip', 'D:\\python\\DLLs', 'D:\\python\\lib', 'D:\\python', 'C:\\Users\\wuwenda\\AppData\\Roaming\\Python\\Python37\\site-packages', 'D:\\python\\lib\\site-packages', 'D:\\python\\lib\\site-packages\\win32', 'D:\\python\\lib\\site-packages\\win32\\lib', 'D:\\python\\lib\\site-packages\\Pythonwin']
b.sort()

for i in a:
    print(i)
for i in b:
    print(i)
