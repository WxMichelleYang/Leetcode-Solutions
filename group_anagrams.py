# Solution 1
# from typing import Dict, List
# class Solution:
#     def genCode(self, word: str) -> str:
#         charCount = [0] * 26
#         for c in word:
#             index = ord(c) - ord('a')
#             charCount[index] += 1
#         code = ""
#         for i in range(26):
#             if charCount[i] > 0:
#                 code += chr(ord('a') + i) + str(charCount[i])
#         return code

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         codeWords: Dict[str, list[str]] = {}
#         for word in strs:
#             code = self.genCode(word)
#             if code in codeWords:
#                 codeWords[code].append(word)
#             else:
#                 codeWords[code] = [word]

#         ret = []
#         for _, words in codeWords.items():
#             ret.append(words)
#         return ret

from typing import Dict
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        codeWords: Dict[tuple, List[str]] = defaultdict(list)
        a = ord('a')
        for word in strs:
            code = [0] * 26
            for c in word:
                code[ord(c) - a] += 1
            codeWords[tuple(code)].append(word)

        return list(codeWords.values())


# Key takeaways:
# 1. directly using tuple as the key of dictionary can reduce the code's complexity 
# 2. using defaultdict(list) to initialize a dictionary will create default entry for an unfound key; 
