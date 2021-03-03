import time
def calculate_time(func):
#	@functools.wraps(func)
	def wrapper_calculate_time():
		start_time = time.perf_count()
		value = func()
		end_time = time.perf_count()
		run_time = end_time - start_time
		print(f'Total time taken to complete function is {run_time} seconds')
		return value
	return wrapper_calculate_time
