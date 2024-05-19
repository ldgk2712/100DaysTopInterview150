class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        
        i = 0
        j = len(s)-1
        s = s.lower()

        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
s = Solution()
print(s.isPalindrome("0P")) # false
