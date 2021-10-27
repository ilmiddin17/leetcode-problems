class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a10=0
        b10=0
        k=0
        for i in a[::-1]:
            a10+=int(i)*(2**k)
            k+=1
        
        k=0
        for i in b[::-1]:
            b10+=int(i)*(2**k)
            k+=1
        st=''
        summa=a10+b10
        while summa>0:
            st+=str(summa%2)
            summa//=2
        return  st[::-1] if len(st)>0 else '0'
            
            
