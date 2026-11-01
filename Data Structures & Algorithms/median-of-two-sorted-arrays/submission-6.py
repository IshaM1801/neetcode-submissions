class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a1,a2=0,0
        l1,l2=len(nums1),len(nums2)
        merge=[]
        while a1 <= l1 or a2<=l2:
            
            if l1==0:
                merge=nums2
                break
            elif l2==0:
                merge=nums1
                break
           
            elif a1==l1:
                for i in range(a2,l2):
                    merge.append(nums2[i])
                break
            elif a2==l2:
                for i in range(a1,l1):
                    merge.append(nums1[i])
                break
            

            elif nums1[a1]<nums2[a2]:
                merge.append(nums1[a1])
                a1+=1
            elif nums1[a1]>nums2[a2]:
                merge.append(nums2[a2])
                a2+=1
            else:
                merge.append(nums1[a1])
                a1+=1
                merge.append(nums2[a2])
                a2+=1
            
        print(merge)
        if len(merge)%2==0:
            return (merge[len(merge)//2]+merge[(len(merge)//2)-1])/2
        else:
            return merge[len(merge)//2]


        