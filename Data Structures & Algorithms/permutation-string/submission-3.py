class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=[0 for i in range(26)]
        if len(s1)>len(s2):
            return False
        
        for i in s1:
            offset=ord(i)-ord('a')
            a[offset]+=1
        l,r=0,len(s1)-1
        a2=[0 for i in range(26)]
        for i in range(l,len(s1)):

            offset=ord(s2[i])-ord('a')
            a2[offset]+=1
        print(a2)
        while r<len(s2):
            if a!=a2:
                a2[ord(s2[l])-ord('a')]-=1
                l+=1
                r+=1
                if r<len(s2):
                    a2[ord(s2[r])-ord('a')]+=1
            else:
                return True
            
            
        

            


        return False
            
        