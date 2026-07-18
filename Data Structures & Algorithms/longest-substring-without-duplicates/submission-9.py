class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        last_index=0
        window=0
        l=len(s)
        ind=0
        max_window=0
        dictionary={}
        while ind<len(s):


            if s[ind] in dictionary:
                max_window=max(window,max_window)
                dictionary.clear()
                temp=last_index
                last_index=ind
                ind=temp
                if temp<l-1:
                    ind=temp+1
                window=0
                
                

            dictionary[s[ind]]=1
            window+=1
            ind+=1
        return max(window,max_window)
        