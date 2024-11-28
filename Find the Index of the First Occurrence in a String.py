class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not(needle in haystack):
            return -1
        else:
            for i in range(len(haystack)):
                if haystack.startswith(needle, i):
                    return i
        