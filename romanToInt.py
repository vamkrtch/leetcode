#include hghjhhoikl;,

class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
       
    
        st = 0
        for i in range(len(s)):
            if i + 1 < len(s) and dict1[s[i]] < dict1[s[i+1]]:
                st -= dict1[s[i]]
            else:
                st += dict1[s[i]]
        return st
