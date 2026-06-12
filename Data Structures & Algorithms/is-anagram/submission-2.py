class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {},{}

        for n in range(len(s)):
            countS[s[n]] = 1 + countS.get(s[n],0)
            countT[t[n]] = 1 + countT.get(t[n],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

