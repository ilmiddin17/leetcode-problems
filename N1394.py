class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lst=[]
        dic={num:0 for num in arr}
        for num in arr:
            dic[num]+=1
        for key, value in dic.items():
            if key==value:
                lst.append(key)
        if len(lst)<1:
            return -1
        else:
            return max(lst)
