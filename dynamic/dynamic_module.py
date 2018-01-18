'''
	Call a function from a module dynamically

'''

import sys,importlib,os

def invoke_module(module_name,func_name,**params):
	sys.path.append(os.path.join('module_dir')) # if module is in different directory from current directory
	dyn_module = importlib.import_module(module_name)
	return getattr(custom_module, func_name)(params=params)

if __name__ == '__main__':
	'''
		'my_module' is the python file name & 'my_func' is the function in that file
	'''
	invoke_module('my_module','my_func',param1='value',param2='value2')




# /module_dir/my_module.py

def my_func(**params):
	print('in my_func')
