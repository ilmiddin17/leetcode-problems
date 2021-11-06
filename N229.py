class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={x:0 for x in nums}
        for num in nums:
            dic[num]+=1
        return [key for key,value in dic.items() if value>len(nums)/3]
