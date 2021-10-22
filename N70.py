from functools import lru_cache

@lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        else:
            return self.climbStairs(n-2)+self.climbStairs(n-1)
