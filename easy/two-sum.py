# 有一种特殊情况，[1,2,7,2,9] target=4, 而且2只能出现最多两次，因为已经限制了只有一个解
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = dict()
        for idx, v in enumerate(nums):
            sub = target - v
            if sub not in ht:
                ht[v] = idx
            else:
                return [ht[sub], idx]
