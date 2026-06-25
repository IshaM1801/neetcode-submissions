class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            

        else:
            i=0
            t=m+n
            j=0
            while i<t and j<n:
                if i>=m and nums1[i]==0:
                    nums1[i]=nums2[j]
                    j+=1
                    i+=1
                elif nums1[i]>=nums2[j]:
                    print (nums1[i],nums2[j])
                    nums1.insert(i,nums2[j])
                    j+=1
                    i=i+1
                    nums1.pop()
                
                elif nums1[i]<nums2[j]:
                    print (nums1[i],nums2[j])
                    i+=1

                print (nums1,nums2)
        

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """