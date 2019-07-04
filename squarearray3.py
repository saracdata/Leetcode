class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        y= list(map(lambda x: x*x, A))
        
        negative =[]
        for i in range(len(A)):
            if A[i] <0:
                negative.insert(0,y[i])
            else:
                midindex=i
                break
        
        positive = y[i:]
                
        newfirst = negative
        last = positive
        
        ##### using last part of merge sort #####
        #make use of sorted nature of the 2 arrays O(nlogn) -> O(n)
        #Because newfirst and last arrays are both sorted: we use the last step of a merge sort: merge step
        
        completeA =[] # check later if len(completeA) = len(last) + len(newfirst)
        
        l=0
        f=0
        while l < len(last) and f < len(newfirst):
            if newfirst[f] > last[l]:
                completeA.append(last[l])
                l+=l
            else:
                completeA.append(newfirst[f])
                f+=1
        while l < len(last):
            completeA.append(last[l])
            l+=1
        while f < len(newfirst):
            completeA.append(newfirst[f])
            f+=1
        
        return completeA
