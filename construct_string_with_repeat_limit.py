Solution 1 main idea:
Greedy: 
every time get as many as possible the largest character, 
so if there are still largest characters left, 
we will need to move forward to find one next largest char to avoid exceeding repeatlimit
if we can't find one, it should stop and return; if yes, append one second largest char;

And repeat 


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        charCount = [0] * 26
        a = ord('a')
        for c in s:
            i = ord(c) - a
            charCount[i] += 1

        ret = ""
        while True:
            i = 25
            while i >=0 and charCount[i] == 0:
                i -= 1
            if i < 0:
                return ret
            repeat = min(repeatLimit, charCount[i])
            print(repeat, chr(a+i))
            ret += chr(a + i) * repeat
            charCount[i] -= repeat
            if repeat == repeatLimit and charCount[i] > 0:
                i -= 1
                while i>=0 and charCount[i] == 0:
                    i -= 1
                if i<0:
                    return ret
                print(f"get one more {chr(a+i)}")
                ret += chr(a + i)
                charCount[i] -= 1
        return ret
