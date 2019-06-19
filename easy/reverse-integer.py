class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(str(s * x)[::-1])
        return s * r * (r < 2**31)
        '''
        sh, ys = x, 0
        if x>(2**31-1) or x < -2**31:
            return 0
        if x < 0:
            sh = -x

        ret = 0

        while sh > 0:
            ys = sh % 10
            sh = sh / 10
            ret = ret * 10 + ys
            if ret>(2**31-1):
                return 0
        if x < 0:
            return -ret
        return ret
        '''
