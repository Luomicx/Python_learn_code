"""
 自定义一个Myrange类，实现range的功能
 只接受两个参数，起始值和步长，实现无限增长
"""

class MyRange:
    """range"""
    
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.value = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        """迭代规则"""
        self.value = self.start
        self.start = self.start + self.step
        return self.value

    def reset(self):
        self.value = 0
    

my_range = MyRange(5, 2)

for i in my_range:
    print()
