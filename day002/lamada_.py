import random
add = lambda x, y: x + y
add(3, 5)

# 使用匿名函数对二维列表排序
arr = [(1, 2), (3, 4), (-1, 12)]
arr.sort(key=lambda x : x[1])
print(arr)

# 使用map函数对arr2数组进行变为字符串
arr2 = []
for i in range(1, 6):
    j = random.randint(1, 6)
    arr2.append(j)
print(arr2)

list1 = list(map(str, arr2))
print(list1)

arr3 = ['Spring', 'Summer', 'Fall', 'Winter']
for index, x in enumerate(arr3):
    print(f"索引是{index}，值是{x}")
    
    
score = [('9.', '1'), ('8.', '8'),
         ('9.', '0'), ('9.', '0'),
         ('9.', '0'), ('8.', '9'),
         ('9.', '1'), ('9.', '3'),
         ('9.', '3'), ('9.', '2')]
name = ['龙猫', '阿飞正传', '爱·回家', '海洋', '我爱你', '黄金三镖客', '迁徙的鸟', '千与千寻', '海上钢琴师',
        '天堂电影院']

# 把分数合并
print(list(map(lambda x: float(x[0] + x[1]), score)))
new_score = list(map(lambda x: float(x[0] + x[1]), score))
# 电影名与分数一一对应
print(list(zip(new_score, name)))
# 筛选 9.0 分以上电影
print(*filter(lambda x: x[1] >= 9.0, zip(name, new_score)))
# 排序 分数从高到低
print(sorted(filter(lambda x: x[1] >= 9.0, zip(name, new_score)), key=lambda x: x[1], reverse=True))
