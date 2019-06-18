class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        hash = {}
        for i, v in enumerate(s):
            if v in hash and start <= hash[v]:
                start = hash[v] + 1
            else:
                max_length = max(max_length, i - start + 1)
            hash[v] = i
        return max_length
