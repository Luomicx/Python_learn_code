import threading
import requests

lock = threading.Lock()  # 创建全局锁

def get_html(url):
    response = requests.get(url)
    return response.text

def save_html(html, name):
    path = '网页'
    file_path = f"{path}\\{name}"
    with lock:  # 加锁保护文件写入
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(html)
    return file_path

def worker(url, name):
    html = get_html(url)
    file_path = save_html(html, name)
    print('保存的文件路径为：', file_path)

if __name__ == '__main__':
    urls = ['http://www.soso.com', 'http://www.baidu.com']
    names = ['soso.html', 'baidu.html']
    
    threads = []
    for url, name in zip(urls, names):
        t = threading.Thread(target=worker, args=(url, name))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()