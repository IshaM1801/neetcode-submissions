class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for ind,i in enumerate(s):
            if i.isalpha() or i.isdigit():
                st += i.lower()
        l=len(s)//2
        r=-1
  
        if not st:
            
            return True
        for i in range(l):
       
            if st[i]==st[r]:
                r-=1
            else:
                return False

       
        return True