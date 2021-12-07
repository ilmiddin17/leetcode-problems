class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        [1,4,2,5,3]
        1, 142, 14253
        4, 425
        2, 253
        5
        3
        
        """
        i=0
        ans=0
        while i<len(arr):
            for j in range(i,len(arr),2):
                ans+=sum(arr[i:j+1])
            i+=1
        return ans
