class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        parsedNumber = str(x)
        left, right = 0, len(parsedNumber) - 1

        while left < right:
            if parsedNumber[left] != parsedNumber[right]:
                return False
            left += 1
            right -= 1
        
        return True