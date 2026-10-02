class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            while i<j and not(97 <= ord(s[i].lower()) <= 122 or 48 <= ord(s[i]) <= 57):
                i+=1
            while i<j and not (97 <= ord(s[j].lower()) <= 122 or 48 <= ord(s[j]) <= 57):
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1

        return True

    #t - o(n)
    #s - o(1)