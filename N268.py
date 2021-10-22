class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>=2:
            num=sum([int(x) for x in str(num)])
            return self.addDigits(num)
        else:
            return num
