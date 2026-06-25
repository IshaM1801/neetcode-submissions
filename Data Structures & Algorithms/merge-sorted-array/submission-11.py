class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            

        else:
            pos=m+n-1
            i=m-1
            j=n-1
            while j>=0 :
                if i>=0 and nums1[i]>nums2[j]:
                    nums1[pos]=nums1[i]
                    i-=1
                    
                else:
                    nums1[pos]=nums2[j]
                    j-=1
                pos-=1
            for i in range(j):
                nums1[i]=nums2[i]
                
                
            
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """