import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.indexes=[]

    def pick(self, target: int) -> int:
        if target in self.nums:
            for i in range(len(self.nums)):
                if self.nums[i]==target:
                    self.indexes.append(i)
            return random.choice(self.indexes)
        else:
            return
            
