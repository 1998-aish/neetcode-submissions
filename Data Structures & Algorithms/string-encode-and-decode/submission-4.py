class Solution:
#'hello','world' -> 'hello0world0'
#'helloworld' -> 'hello','world'
# 4#hello5#world
# ij

    def encode(self, strs: List[str]) -> str:
        str1=[]
        for i in strs:
            str1.append(str(len(i)))
            str1.append('#')
            str1.append(i)
        return ''.join(str1)
     
        
    def decode(self, s: str) -> List[str]:
        arr=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            arr.append(s[i:j])
            i=j
            
        return arr

