class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newString = ""

        for x in s:
            if x.isalnum() == True:
                newString += x
        
        if len(newString) == 0 or len(newString) == 1:
            return True

        for i in range(0, len(newString)-1, 1):
            j = len(newString)-i-1
            if i == j:
                return True
            elif newString[i] != newString[j]:
                return False
            elif (j - i) == 1:
                return True