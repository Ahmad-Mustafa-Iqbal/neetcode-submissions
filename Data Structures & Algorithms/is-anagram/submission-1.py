class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len (t):
            return False
        
        c = {}

        for ch in s:
            c[ch] = c.get(ch,0)+ 1
        
        for ch in t:
            if ch not in c or c[ch] ==0:
                return False
            c[ch] -= 1

        return True 