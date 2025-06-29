PI = 3.1415926
e = 2.712

def global_test_func():
	global PI
	print(f"global Pi = {PI}")
	print('local e = {}'.format(e))

global_test_func()