class Solution(Object):
    def process(self, nums, target):
        ret = None
        diff = None
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return tmp
                elif tmp < target:
                    if diff == None or diff > target - tmp:
                        diff = target - tmp
                        ret = tmp
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif tmp > target:
                    if diff == None or diff > tmp - target:
                        diff = tmp - target
                        ret = tmp
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ret
