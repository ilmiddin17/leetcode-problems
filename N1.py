class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        k=len(nums)
        while i+1<k:
            for j in range(i+1,k):
                if nums[i]+nums[j]==target:
                    return [i,j]
            else:
                i+=1
            
