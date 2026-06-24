class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = [0] * 26
        d={}
        o={}
        for w in strs:
            for l in w:
                c[ord(l)-ord('a')]+=1
            k=tuple(c)
            if k in d:
                
                d[k].append(w)
            else:
                d[k]=[]
                d[k].append(w)
            c = [0] * 26
        
        return list(d.values())

        