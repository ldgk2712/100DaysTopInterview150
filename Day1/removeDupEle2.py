class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k

# Time complexity: O(n)
s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3])) # 5