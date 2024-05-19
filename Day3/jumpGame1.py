class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy algorithm
        # Time complexity: O(n)
        # Space complexity: O(1)
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
    
s = Solution()
print(s.canJump([2,3,1,1,4])) # True
print(s.canJump([3,2,1,0,4])) # False
print(s.canJump([2,0])) # True
print(s.canJump([1,2,3])) # True