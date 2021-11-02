class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m1=min(nums)
        m2=max(nums)
        ekub=1
        
        for i in range(1,m1+1):
            if m1%i==0 and m2%i==0:
                ekub=i
        return ekub
