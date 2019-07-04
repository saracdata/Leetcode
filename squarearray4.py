class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """        
        negative =[]
        for i in range(len(A)):
            if A[i] <0:
                negative.insert(0,A[i])
            else:
                midindex=i
                break
                
        positive = A[i:]
        ##### using last part of merge sort #####
        #make use of sorted nature of the 2 arrays O(nlogn) -> O(n)
        #Because newfirst and last arrays are both sorted: we use the last step of a merge sort: merge step
        
        completeA =[] # check later if len(completeA) = len(positive) + len(negative)
        
        l=0
        f=0
        while l < len(positive) and f < len(negative):
            if negative[f]**2 > positive[l]**2:
                completeA.append(positive[l]**2)
                l+=l
            else:
                completeA.append(negative[f]**2)
                f+=1
        while l < len(positive):
            completeA.append(positive[l]**2)
            l+=1
        while f < len(negative):
            completeA.append(negative[f]**2)
            f+=1
        
        return completeA
