class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        value = n 
        while value > 0:
            count += value // 5
            value = value // 5

        return count