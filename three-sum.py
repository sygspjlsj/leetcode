class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1] or nums[i] > 0:
                continue
            l, r = i + 1, length - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    # have compared
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif target < 0:
                    # not have compared
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif target > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ret
