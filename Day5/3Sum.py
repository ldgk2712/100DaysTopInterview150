class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lst = []
        for i in range(len(nums)):
            # Skip duplicate element
            if i > 0 and nums[i] == nums[i-1]:
                continue    
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    lst.append([nums[i],nums[l],nums[r]])
                    l += 1
                    # Skip duplicate element
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return lst

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]