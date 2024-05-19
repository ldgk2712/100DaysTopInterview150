class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        n = len(height)-1
        j = len(height)-1
        maxArea = 0

        while i < j:
            if height[i] < height[j]:
                area = height[i] * n
                i += 1
            else:
                area = height[j] * n
                j -= 1
            n -= 1
            maxArea = max(maxArea,area)
        return maxArea

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49