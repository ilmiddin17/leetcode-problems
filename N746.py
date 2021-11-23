class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first=cost[0]
        second=cost[1]
        l=len(cost)
        if l<3:
            return min(first,second)
        for i in range(2,l):
            cur=cost[i]+min(second, first)
            first=second
            second=cur
        return min(first, second)
