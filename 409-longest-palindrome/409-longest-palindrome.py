class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        odd = 0
        for char in set(s):
            if s.count(char)%2 == 0:
                count += s.count(char)
            else:
                count += s.count(char)-1
                odd += 1
        if odd > 0:
            count += 1

        return count