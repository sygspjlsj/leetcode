class Solution(object):
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in xrange(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(ret):
                ret = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(ret):
                ret = tmp
        return ret
