class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        count=1
        cur=0
        for i in range(1,n):
            if nums[cur]!=nums[i]:
                nums[cur+1], nums[i] = nums[i],nums[cur+1]
                count+=1
                cur+=1
        return count
