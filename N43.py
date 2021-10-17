class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        n1=0
        k=1
        for i in num1[::-1]:
            n1+=dict.get(i)*k
            k=k*10
        n2=0
        l=1
        for j in num2[::-1]:
            n2+=dict.get(j)*l
            l=l*10
        return str(n1*n2)
            
