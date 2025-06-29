import time
import threading
import random

urls = [
    f'http://www.baidu.com?page={page}' for page in range(100)
]

lock = threading.Lock()


def download(url, no, name=None):
    time.sleep(random.random())
    with open('demo.txt', mode='a', encoding='utf-8') as f:
        lock.acquire()
        f.write(f'no:{no} name:{name} url:{url}\n')
        lock.release()
    return None 


start_time = time.time()
no = 1
for url in urls:
    # download(url, name='百度')
    download_thread = threading.Thread(target=download, args=(url, no), kwargs={'name': 'baidu'})
    download_thread.start()
    no += 1