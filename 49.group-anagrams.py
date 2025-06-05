from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if (dic.get(key, -1) == -1):
                dic[key] = []
            dic[key].append(s)
        
        ret = []
        for key, value in dic.items():
            ret.append(value)
        return ret