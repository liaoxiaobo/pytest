import pytest
from pycode.calculator import Calculator


# 所有同目录测试文件运行前都会执行conftest.py，autouse=true是设定都会调用此函数
@pytest.fixture()
def cal_init():
	cal = Calculator()
	print('开始计算')
	yield cal
	print('结束计算')
