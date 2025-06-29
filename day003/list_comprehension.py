squares = [x**2 for x in range(1, 11)]

# 从 1 到 10 中筛选出偶数，并计算它们的平方。
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# 两两合并
letters = ['a', 'b', 'c']
numbers = [1, 2]
pairs = [(letters, numbers) for letter in letters for number in numbers]