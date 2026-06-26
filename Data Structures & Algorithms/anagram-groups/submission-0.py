from collections import defaultdict 
from typing import List 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        am= defaultdict(list)

        for s in strs:
            count = [0]*26

            for alp in s:
                count[ord(alp)-ord('a')]+=1

            am[tuple(count)].append(s)
        return list(am.values())
