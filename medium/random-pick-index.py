import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(
            [k for k, v in enumerate(self.nums) if v == target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
