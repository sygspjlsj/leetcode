class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, m, n = 0, 0, len(s), len(p)
        while i < m and j < n:
            if p[j] == s[i]:  # character
                i += 1
                j += 1
            elif p[j] == '*':  # *
                if i - 1 >= 0:
                    pass
            elif p[j] == '.':  # .
                pass
