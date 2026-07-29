class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        d = len(matrix)
        i = 0
        while i <(d - 1 - i):
            last = d-1-i
            for k in range(last - i):
                # saved_value = matrix[last-k][i]
                # matrix[last-k][i] = matrix[last] [last-k]
                # matrix[last][last-k] = matrix[i+k][last]
                # matrix[i+k][last] = matrix[i][i+k]
                # matrix[i][i+k] = saved_value
                matrix[i][i+k], matrix[last-k][i], matrix[last][last-k], matrix[i+k][last]= matrix[last-k][i],matrix[last][last-k],matrix[i+k][last],matrix[i][i+k]
            i += 1
            
# Key takeaways:
# 1. using last to replace d-1-i can reduce runtime significantly 
# 2. use Python's tuple swap
# 3. rotate 90 (clockwise) = transpose + reverse every row