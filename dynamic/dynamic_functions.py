'''
call functions dynamically
'''
import sys

def show():
	print('in show')

def show_():
	print('in show_')

class DynamicFunction:

	def class_show(self):
		print('in class_show')

	def class_show_params(self,param1):
		print('in class_show_params with params {}'.format(param1))

if __name__ == '__main__':

	'''
		Call function which is not in any class
	'''
	method_name = 'show'
	getattr(sys.modules[__name__],method_name)()

	'''
		Call function which is not in any class
		and even part of method name is dynamic
	'''
	method_name = 'show'
	getattr(sys.modules[__name__],method_name+'_')()

	'''
		Call function in class
	'''
	method_name = 'class_show'
	dyn_func = DynamicFunction()
	getattr(dyn_func,method_name)()

	'''
		Call function in class with parameters
	'''
	method_name = 'class_show_params'
	dyn_func = DynamicFunction()
	getattr(dyn_func,method_name)("param1 value")
