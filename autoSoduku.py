#!/usr/bin/python3


num = [
[0,6,0,1,7,8,0,2,0],
[0,0,0,0,0,0,0,0,0],
[0,0,2,0,6,0,4,0,0],
[0,0,5,0,0,0,2,0,0],
[3,2,0,0,0,0,0,6,4],
[0,9,6,0,4,0,8,7,0],
[5,0,0,4,0,1,0,0,8],
[2,0,0,6,8,3,0,0,9],
[0,0,0,0,0,0,0,0,0],
]

class Soduku(object):
	def __init__(self, num):
		self.num = num
		self.temp = []
		self.position = [] # record the positon of 

	def calSquare(self,x,y):
		pass

	def calRow(self,x,y):
		pass

	def calCol(self):
		pass

	def calAllEmpty(self):
		# cal all empty possible values
		for outer_index in range(9):
			for inner_index in range(9):
				pass

	def  checkRow(self, testValue, rowNumber):
		# True if the values in this row is uniqe 		
		if testValue in self.num[rowNumber]:
			return False
		else:
			return True

	def checkCol(self, testValue, colNumber):
		if testValue in [ele[colNumber] for ele in self.num]:
			return False
		else:
			return True

	def checkSquare(self, testValue, x, y):
		borderX = x // 3 * 3
		borderY = y // 3 * 3

	def loop(self):
		pass



if __name__ == "__main__":
	obj = Soduku(num)
	print(obj.checkRow(3,0))
	print(obj.checkCol(7,0))


