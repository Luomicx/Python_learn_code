import random

card_data = [
	['1', '⽩雪公主', '5', '4', '2', '2'],
	['2', '睡美⼈', '7', '5', '1', '5'],
	['3', '灰姑娘', '9', '3', '8', '7'],
	['4', '美⼈⻥', '6', '7', '10', '1'],
	['5', '花⽊兰', '8', '10', '9', '6'],
	['6', '阿拉丁', '4', '6', '3', '9'],
	['7', '爱莎', '3', '8', '4', '4'],
	['8', '勇敢骑⼠', '1', '9', '5', '3'],
]

class Dice:
	@staticmethod
	def dice():
		return random.randint(1, 6)

class Card:
	attr_name = ['iq', 'power', 'speed', 'attack']
	def __init__(self, no, name, iq, power, speed, attack):   
		self.no = no
		self.name = name
		self.iq = iq
		self.power = power
  

	