class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dct = {}
        direction = -1
        curr = 0
        for i in range(numRows):
            dct[i] = []
        for i in range(len(s)):
            dct[curr].append(s[i])
            if curr == 0 or curr == numRows - 1:
                direction = 0 - direction
            curr += direction
        ret = ''
        for i in dct:
            ret += ''.join(dct[i])
        return ret
