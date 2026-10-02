class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in s.lower():
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                arr.append(i)
        i=0
        l=len(arr)-1
        while i<l:
            if arr[i]!=arr[l]:
                return False
            i+=1
            l-=1     
        return True

    #time = o(n)
    #space = o(n)