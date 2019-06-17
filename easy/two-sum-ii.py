class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        g = len(numbers) - 1
        if l >= g:
            return [-2, -1]
        while l < g:
            ret = numbers[l] + numbers[g]
            if ret == target:
                return [l + 1, g + 1]
            elif ret < target:
                l += 1
            elif ret > target:
                g -= 1
        '''
        for i in xrange(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] > tmp:
                    r = mid - 1
                else:
                    l = mid + 1
        '''
