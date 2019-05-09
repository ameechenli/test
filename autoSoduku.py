#!/usr/bin/python3


num = [
    [0, 1, 0, 0, 0, 0, 0, 0, 5],
    [4, 0, 0, 0, 2, 0, 0, 0, 0],
    [8, 0, 0, 7, 0, 0, 0, 9, 0],
    [0, 0, 6, 0, 0, 5, 0, 2, 0],
    [0, 9, 0, 0, 6, 0, 0, 3, 0],
    [0, 4, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 0, 1, 0, 0, 4],
    [0, 0, 0, 0, 9, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 5, 0],
]


class Soduku(object):
    def __init__(self, num):
        self.num = num
        self.temp_num = []
        self.position = []  # record the empty position

    def getSquare(self,x,y):
        borderX = x // 3 * 3
        borderY = y // 3 * 3
        temp = []
        for row in range(9):
            for col in range(9):
                if borderX <= col < borderX + 3 and borderY <= row < borderY + 3 and self.num[row][col]:
                    temp.append(self.num[row][col])
        return temp

    def calSquare(self, x, y):
        return self.getSquare(x, y)

    def calRow(self, y):
        temp = []
        for ele in self.num[y]:
            if ele:
                temp.append(ele)
        return temp

    def calCol(self, x):
        temp = []
        for row in range(9):
            if self.num[row][x]:
                temp.append(self.num[row][x])
        return temp

    def calAllEmpty(self, x, y):
        # cal all empty possible values
        temp_s = self.calSquare(x, y)
        # print('square is :', temp_s)
        temp_c= self.calCol(x)
        # print('col is ,', temp_c)
        temp_r= self.calRow(y)
        # print('row is ,', temp_r)
        temp = temp_c + temp_r + temp_s
        result = []
        for ele in range(1, 10):
            if ele not in temp:
                result.append(ele)
        return result

    def checkRow(self, testValue, rowNumber):
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
        temp = self.getSquare(x,y)
        # print('getSquare:', temp)
        if testValue in temp:
            return False
        else:
            return True

    def recoderEmpty(self):
        for row in range(9):
            for col in range(9):
                if self.num[row][col] == 0:
                    self.position.append(str(row)+str(col))

    def loop(self, x, y):
        print()
        [print(ele) for ele in self.num]
        print("index is y x  ", str(y)+str(x))
        # input("pause here and type to pass***********\n")
        temp = self.calAllEmpty(x, y)
        print('get the temp value', temp)
        for ele in temp:
            if self.checkCol(ele, x) and self.checkRow(ele, y) and self.checkSquare(ele, x, y):
                # print('now pass ', ele, "index is ", str(y)+str(x))
                self.num[y][x] = ele
                # get the next index
                index = self.getIndex(x, y)+1
                if index >= len(self.position):
                    print("finally result:**********\n\n")
                    [print(ele) for ele in self.num]
                    break
                else:
                    x = int(self.position[index][1])
                    y = int(self.position[index][0])
                    # print("next x y is ", x, y)
                    self.loop(x, y)
            else:
                print('continue')

        else:
            # print('now not pass', "index is ", str(y) + str(x))
            # get last index
            index = self.getIndex(x, y) - 1
            if index < 0:
                print('index error !')
            x = int(self.position[index][1])
            y = int(self.position[index][0])
            self.num[y][x] = 0

    def getIndex(self, x, y):
        index = self.position.index(str(y)+str(x))
        return index

    def start(self):
        self.recoderEmpty()
        # print(self.position)
        # input()
        x = int(self.position[0][1])
        y = int(self.position[0][0])
        self.loop(x, y)


if __name__ == "__main__":
    [print(ele) for ele in num]
    obj = Soduku(num)
    # print(obj.checkRow(4, 0))
    # print(obj.checkCol(4, 0))
    # print(obj.checkSquare(4, 0, 0))
    obj.start()


