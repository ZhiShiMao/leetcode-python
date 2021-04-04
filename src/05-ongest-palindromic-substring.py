class Solution:
    def longestPalindrome(self, s: str) -> str:
        """给你一个字符串 s，找到 s 中最长的回文子串。"""

        ret = ""
        for i in range(len(s)):
            x, y = i - 1, i + 1
            while x >= 0 and y <= len(s) - 1:
                if s[x] != s[y]:
                    break
                x -= 1
                y += 1
            if len(s[x + 1 : y]) > len(ret):
                ret = s[x + 1 : y]

            x, y = i, i + 1
            while x >= 0 and y <= len(s) - 1:
                if s[x] != s[y]:
                    break
                x -= 1
                y += 1
            if len(s[x + 1 : y]) > len(ret):
                ret = s[x + 1 : y]

        return ret


s = Solution()
r = s.longestPalindrome("ac")
print(r)