# ------------ 直线方程配置 ------------ #
def line_conf(a, b):
    def line(x):
        print("x = " ,x)
        return a * x + b
    print("y = {}*x + {}".format(a, b))
    return line


line1 = line_conf(2, 1)
print("y =", line1(5), "\n")



def filter_url(func):
    def wrapper(*args, **kwargs):
        if 'maoyan' in kwargs['url']:
            result = func(*args, **kwargs)
            print('下载成功', kwargs['url'])
            return result
        else:
            print('不是猫眼网站的网址', kwargs['url'])
    return wrapper