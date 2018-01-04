"""
This is an advanced decorator which performs profiling to various methods
in the application. Use it above the method for which you want to do profiling.
With below script , default profiling is disabled. if you want to enable pass
'-p=True' Or '-profiling=True' while running your script to enable it.

By default, this will sort the statistics based on 'cumulative' and will show top three stats
containing methods of your file only and skip the python library files.

This is very useful for measuring performance of your  application.

This decorator is very generic and you can pass any number of parameters like sort_col,no_of_rec.

Usage : 

@do_cprofile(__file__)
def my_method():


Refer app.py for usage example

"""

import cProfile
import pstats,sys


def do_cprofile(file_name,**kwargs):
	arguments = kwargs
	def create_profiler(func):	
		def profiled_func(*args, **kwargs):
			
			profile = cProfile.Profile()
			try:
				profile.enable()
				result = func(*args, **kwargs)
				profile.disable()
				return result
			finally:
				profiling_args = ['-p=True','-profiling=True']  # line-1 : pass parameter to enable profiling
				stat_file = '/profiling_stats.txt'
				if any(i in profiling_args for i in sys.argv):
					profile.dump_stats(stat_file)
					p = pstats.Stats(stat_file)
					print('=============================================')
					p.sort_stats(arguments.get('sort_col','cumulative')).print_stats(arguments.get('no_of_rec',3),file_name)
		return profiled_func
	return create_profiler
