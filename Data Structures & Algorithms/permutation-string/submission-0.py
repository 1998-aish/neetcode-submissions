class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # char1={}
        char2={}
        for ch in s1:
                if ch in char2:
                    char2[ch]+=1
                else:
                    char2[ch]=1
        for i in range(len(s2)- len(s1) + 1):
            char1={}
            for ch in s2[i:i + len(s1)]: 
                if ch in char1:
                    char1[ch]+=1
                else:
                    char1[ch]=1
            if char1 == char2:                     # same letters and counts?
                return True
    
        return False

        
        