class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        after=set()
        morse={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        for i in words:
            imp=''
            for j in i:
                imp+=morse.get(j)
            after.add(imp)
        return len(after)
                
        
