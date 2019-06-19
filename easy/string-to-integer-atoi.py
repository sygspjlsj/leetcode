class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ret = ''
        str = str.strip()
        for i in range(len(str)):
            if i == 0 and str[i] in ('+',
                                     '-') or str[i] >= '0' and str[i] <= '9':
                ret += str[i]
            else:
                break
        if ret == '':
            return 0
        s = 1
        l = ''
        if ret[0] == '-':
            s = -1
            l = ret[1:]
        elif ret[0] == '+':
            l = ret[1:]
        else:
            l = ret
        if l == '':
            return 0
        if s * int(l) > 2**31 - 1:
            return 2**31 - 1
        elif s * int(l) < -2**31:
            return -2**31
        else:
            return s * int(l)
        return s * int(l) * (int(l) < 2**31)
