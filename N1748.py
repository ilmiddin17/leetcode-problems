class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        dic={num:0 for num in nums}
        for num in nums:
            dic[num]+=1
        for key, value in dic.items():
            if value==1:
                sum+=key
        return sum
