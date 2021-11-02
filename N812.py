class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area=0
        l=len(points)
        for i in range(l-2):
            x1,y1=points[i]
            for j in range(i+1, l-1):
                x2,y2=points[j]
                for k in range(j+1, l):
                    x3,y3=points[k]
                    if abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) > area :
                        area = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    
        return area
