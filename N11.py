#I've seen the solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea,left, right=0,0,len(height)-1
        
        while left<right:
            maxarea=max(maxarea, min(height[left], height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
    
#This is my own solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        return min(height[j],height[i])*(j-i)
        
        """
        i,j=0,len(height)-1
        m=0
        while i<=j:
            if height[i]>height[j]:
                m=max(m, height[j]*(j-i))
                j-=1
            elif height[i]<height[j]:
                m=max(m, height[i]*(j-i))
                i+=1
            else:
                m=max(m,height[i]*(j-i))
                i+=1
                j-=1
        return m
                    
