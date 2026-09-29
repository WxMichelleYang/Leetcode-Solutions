class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        max_val = n - 1
        num_freq = [0] * n
        for num in nums:
            if num > max_val:
                return False
            num_freq[num] += 1
        if num_freq[0] != 0:
            return False
        if num_freq[max_val] != 2:
            return False
        for i in range(1,n-1):
            if num_freq[i] != 1:
                return False
        return True

# Since the max length of nums is 100, 
# it's ok to use a list num_freq to keep the frequency of every number in nums
# if the length of input array is N, and max valid value of nums is N-1
# and the length of num_freq is also N;
# the value of num_freq should be:
# index 0 1 2 3 ... N-2 N-1
# value 0 1 1 1 ... 1    2

# Scan all the numbers in nums, can calculate the freq of every number in num_freq
# and check if num_freq is as expected.

# Time complexity: O(N+N)
# Space complexity: O(N)