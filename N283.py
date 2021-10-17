class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        i=0
        n=len(nums)
        while z<n and i<n:
            if nums[i]==0:
                i+=1
            else:
                nums[z],nums[i]=nums[i],nums[z]
                i+=1
                z+=1
