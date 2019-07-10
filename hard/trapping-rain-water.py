class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        l, r, ans = 0, length - 1, 0
        while l < r:
            val = min(height[l], height[r])
            if val == height[l]:
                l += 1
                while l < r and height[l] < val:
                    ans += val - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and height[r] < val:
                    ans += val - height[r]
                    r -= 1
        return ans
