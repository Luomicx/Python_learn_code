# len函数 ， 可以返回对象的长度（条目的数量），也可以用于实现了 __len__()方法的对象
class A:
    def __len__(self):
        return 10
a = A()
# print(len(a))

# id 返回一个对象的 identity 。它是一个整数，它在其生命周期中保证对这个对象唯一且恒定。具有非重叠生命周期的两个对象可能具有相同的 id() 值。 这是内存中对象的地址。
arr = [1, 2, 3]
# print(id(arr))

# getattr(object, attribute, default) 操作属性的方法
# getattr(user, 'name') == user.name

# setattr(object, name, value) 设置属性通过反射
# setattr(user, 'age', 18) == user.age = 19

# delattr(object, attribute)
# hasattr(object, name)

# divmod 返回商和余数
# print(divmod(10, 3))


# 特殊函数
# property(fget=None, fset=None, fdel=None, doc=None)

class B:
    def __init__(self):
        self._x = None
    
    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value
    
    def del_x(self):
        del self._x
        
    x = property(get_x, set_x, del_x, "I'm the property for X")
    
    
    
# with open('mydata.txt') as fp:
#     for i in iter(fp.readline, ''):
#         process_line(i)
        
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s = slice(1, 8, 2) # 表示从 1 开始一直到 8 的位置，步长为 2

print(a[s])
# [1, 3, 5, 7]
	   
 
 
		
