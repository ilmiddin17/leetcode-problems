class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        [1]
        2,3,5-> 2
        1,1,1-> 2,1,1
        4,3,5-> 3
        2,2,1
        4,6,5-> 4
        3,2,1
        6,6,5->5
        3,2,2
        6,6,10-> 6
        4,3,2
        8,9,10
        
        
        """
        
        dp=[1]*(n+1)
        f2,f3,f5=1,1,1
        
        for i in range(2,n+1):
            p2=dp[f2]*2
            p3=dp[f3]*3
            p5=dp[f5]*5
            
            m=min(p2,p3,p5)
            dp[i]=m
            if m==p2:
                f2+=1
            if m==p3:
                f3+=1
            if m==p5:
                f5+=1
           
                
        return dp[n]
