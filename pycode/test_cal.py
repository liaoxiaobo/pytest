import pytest
import yaml

@pytest.mark.parametrize('a,b', yaml.safe_load(open("./conf_data.yml")))
class TestCal:
	# def setup_class(self):
	# 	self.cal = Calculator() #初始化一个对象实例

	def test_add(self,cal_init,a,b):
		# assert self.cal.add(a,b) == a + b
		assert cal_init.add(a,b) == a + b

	def test_sub(self,cal_init,a,b):
		assert cal_init.sub(a,b) == a - b

	def test_mult(self,cal_init,a,b):
		assert cal_init.mult(a,b) == a * b

	def test_div(self,cal_init,a,b):
		assert cal_init.div(a,b) == a / b