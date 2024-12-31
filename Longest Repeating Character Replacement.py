class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countReps = {}
        longestRep = 0

        l, r = 0, 0
        while r < len(s):
            countReps[s[r]] = 1 + countReps.get(s[r], 0)

            window = s[l : r + 1 :]
            if (len(window) - max(countReps.values())) <= k:
                longestRep = len(window)
            else:
                countReps[s[l]] -= 1
                l += 1
            r += 1

        return longestRep