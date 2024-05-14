class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        k = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                k = nums[i]
            if nums[i] == k:
                count += 1
            else:
                count -= 1
        return k

s = Solution()
print(s.majorityElement([3,2,3])) # 3