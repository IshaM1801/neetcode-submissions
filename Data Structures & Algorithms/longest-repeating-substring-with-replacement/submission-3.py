class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        a = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        
        left,right=0,0
        window=0
        l=len(s)
        while right<l:
            a[s[right].lower()]+=1
            replacements=right-left+1-max(a.values())
            
            if replacements>k:
                while replacements>k:
                    a[s[left].lower()]-=1
                    
                    left+=1
                    replacements=right-left+1-max(a.values())
            
            
            window=max(window,right-left+1)
            right+=1
            

        print(a)
        return window
        