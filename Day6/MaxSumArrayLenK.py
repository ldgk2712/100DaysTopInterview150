class Solution(object):
    def MaxSumArrayLenK(self, nums, k):
        """
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0

        for i in range(k):
            sum += nums[i]
        res = sum

        for i in range(k,len(nums)):
            sum = sum - nums[i-k] + nums[i]
            if sum > res:
                res = sum
        return res

s = Solution()
print(s.MaxSumArrayLenK([1,2,3,1,5,2,7,8,9,1],3)) # 24 [7,8,9]