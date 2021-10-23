class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l=len(nums)/2
        arr={x:0 for x in nums}
        for num in nums:
            arr[num]+=1
        for value, key in arr.items():
            if key==l:
                return value
