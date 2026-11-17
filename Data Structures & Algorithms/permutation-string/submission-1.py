class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Input: s1 = "abc", s2 = "lecabee"
        k=len(s1)
        if len(s1)>len(s2):
            return False
        char1={}
        char2={}
        for ch in s1:
            char1[ch] = char1.get(ch, 0) + 1
        for r in range(len(s2)):
            char2[s2[r]] = char2.get(s2[r], 0) + 1
            if r >=k:
                left=s2[r-k]
                char2[left]-=1
                if char2[left] == 0:
                    del char2[left]
            if char2 == char1:
                return True
        return False






