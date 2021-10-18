import pdb
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # pdb.set_trace()
        prev_map = {}
        for i, num in enumerate(nums):
            if target-num in prev_map:
                return [prev_map[target-num], i]
            prev_map[num] = i

nums = [-1,-2,-3,-4,-5]
target = -8
output = Solution().twoSum(nums, target)
print(output)
