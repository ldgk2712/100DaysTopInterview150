class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0 
        i = 0
        j = 0
        minK = -1
        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                if minK == -1 or minK > j-i+1:
                    minK = j-i+1
                sum -= nums[i]
                i += 1
            j += 1
        if minK == -1:
            return 0
        return minK
    
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2 [4,3]