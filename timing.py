import time
def calculate_time(func):
	def wrapper_calculatetime():
		start = time.time()
		func()
		#time.sleep(3)
		stop = time.time()
		X=stop-start-time.sleep(2)
		print(f'Total time {X}')
	return wrapper_calculatetime
