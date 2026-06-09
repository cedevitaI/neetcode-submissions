class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum()])

        if len(s) == 1: return True

        start = 0
        end = len(s)-1
        while start<=end:
            if s[start]!=s[end]:
                return False
                break
            start += 1
            end -= 1
        return True