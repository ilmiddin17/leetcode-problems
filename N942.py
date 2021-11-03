class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l=len(s)
        perm=[]
        j=0
        for i in s:
            if i=='I':
                perm.append(j)
                j+=1
            else:
                perm.append(l)
                l-=1
        perm.append(j)
        return perm
