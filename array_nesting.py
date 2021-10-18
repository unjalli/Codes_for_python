class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [[] for i in range(len(nums))]
        l = 0
        for i in range(len(nums)):
            j = i
            while nums[j] not in s[i]:
                s[i].append(nums[j])
                j = nums[j]
            if len(s[i]) > l:
                l = len(s[i])
        return l

nums = [5,4,0,3,1,6,2]
l = Solution().arrayNesting(nums)
print(l)
