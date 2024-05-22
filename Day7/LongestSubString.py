class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # using sliding window
        l = maxL = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1   
            char_set.add(s[r])
            maxL = max(maxL, r-l+1)
        return maxL

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # 3 abc