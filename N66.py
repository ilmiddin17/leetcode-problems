class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=1
        s=0
        for i in digits[::-1]:
            s+=k*i
            k*=10
        return [int(x) for x in str(s+1)]
