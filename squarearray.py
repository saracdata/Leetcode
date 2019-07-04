class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        y= list(map(lambda x: x*x, A))
        mid = y.index(y[int(len(y)/2)]) #mid index
        
        # finding the mid value that separates positive and negative values
        
        if A[mid] <0: #means we didnt find the point of separation of positive and negative values
            for i in range(len(y[mid:])-1):
                if A[mid+i+1] <0:
                    continue
                else:
                    newmid =A[mid+i+1]
        elif A[mid]>0:
            for i in range(len(y[:mid])):
                if A[mid-i-1] >0:
                    continue
                else:
                    newmid = A[mid-i+1]
        else: 
            newmid = A[mid]
        # newmid, the value of mid that separates positive and negative values
        # A.index('newmid') #location index of the best separation point
        
        last = y[A.index(newmid):] #last half including mid aka. the positive number half
        first = y[:A.index(newmid)] #first half aka. the negative number half
        newfirst = []
        for j in range(len(first)):
            newfirst.append(first[-j-1])
            return newfirst #reverse the negative numbers from descending to ascending values
        
        
        ##### using last part of merge sort #####
        #make use of sorted nature of the 2 arrays O(nlogn) -> O(n)
        #Because newfirst and last arrays are both sorted: we use the last step of a merge sort: merge step
        
        completeA =[None]*(len(last) + len(newfirst)) # check later if len(completeA) = len(last) + len(newfirst)
        
        c=0
        l=0
        f=0
        while l < len(last) and f < len(newfirst):
            if newfirst[f] > last[l]:
                completeA[c]=last[l]
                l+=l; c+=1
            else:
                completeA[c] = newfirst[f]
                f+=1; c+=1
        while l < len(last):
            completeA[c] = last[l]
            l+=1; c+=1
        while f < len(newfirst):
            completeA[c] = newfirst[f]
            f+=1; c+=1
        
        A = completeA
        return A
