class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        isValid = True
        for i in range(len(text)):
            if text[i] == "%":
                isValid = False
        
        if (isValid):
            return text
        
        dic = {}
        for r in replacements:
            dic[r[0]] = r[1]
        
        r = text.split("%")
        ret = []
        for rr in r:
            if dic.get(rr, -1) == -1:
                if rr == "":
                    continue
                ret.append(rr)
            else:
                ret.append(dic[rr])
        return self.applySubstitutions(replacements, "".join(ret))