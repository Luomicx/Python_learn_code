import time
import threading

def work():
	"""只有函数对象才能使用多线程"""
	print("5.洗茶杯：1min")
	time.sleep(1)
	print("6.洗茶叶: 1min")
	time.sleep(1)
 

start_time = time.time()
print('1. 洗壶：1min')
time.sleep(1)
print('2. 灌凉水：1min')
time.sleep(1)
print('3. 烧水：1min')
time.sleep(1)
print('4. 等水烧开：3min')

work_thread = threading.Thread(target=work)
work_thread.start()
time.sleep(1)  # 5. 洗茶杯：1min
time.sleep(1)  # 6. 放茶叶：1min
time.sleep(1)