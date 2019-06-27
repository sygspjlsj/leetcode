class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, g = 0, len(nums) - 1
        while l <= g:
            mid = (l + g) / 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                g = mid - 1
            else:
                return mid
        return -1
