from collections import defaultdict
class Solution:
    def _toMask(self, c: str):
        if c == 'a':
            return 1
        if c == 'e':
            return 1 << 1
        if c == 'i':
            return 1 << 2
        if c == 'o':
            return 1 << 3
        if c == 'u':
            return 1 << 4
        return 0
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        prefixBits = defaultdict(int)
        prefixBits[0] = -1
        prevBits = 0
        maxLen = 0
        for i in range(n):
            curVal = self._toMask(s[i])
            prevBits ^= curVal
            
            if prevBits in prefixBits:
                j = prefixBits[prevBits]
                maxLen = max(maxLen, i-j)
            else:
                prefixBits[prevBits] = i
        return maxLen

# The brute force solution is to check every substring, s[i:j+1]
# if it contains each vowel an even number of times, so the best time complexity of this 
# method should be O(n^2);
# So we'll optimize it 
# Since we only care if the number of a vowel is even or odd, given a vowel, if it appears 
# odd times, we can use 1 to represent its frequency; and if it appears even number 
# of times, we use 0 to represent its frequency; 
# And since there are 5 vowels to be considered, and we only want to use 0 and 1 
# to represent their frequencies; 
# therefore, for a substr s[:j+1] the number of times of each vowel appears in the substr
# can be represented as a binary number: 
# a e i o u
# 0 1 0 1 0
# so if we can find another substring s[:i+1], where the frequencies of every vowel can 
# also be represented as the same value, the substr s[i:j+1] should contains even numbers
# of vowels.
# The time complexity of this method is O(n)


            
