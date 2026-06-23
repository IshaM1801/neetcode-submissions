class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        a={}
        if len(s)!=len(t):
            return False
        for l in s:
            if l in d:
                d[l]+=1
                continue
            d[l]=0
        for w in t:
            if w in a:
                a[w]+=1
                continue
            a[w]=0
        
        return a==d
        
        