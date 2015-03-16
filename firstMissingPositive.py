class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i=0
        while i<len(A):
            if A[i]>=1 and A[i]<=n and A[i]!=A[A[i]-1] and A[i]!=i+1:
                p=A[i]
                A[i], A[p-1] = A[p-1], A[i]
            else:
                i+=1
        for i in len(A):
            if A[i]!=i+1:
                return i+1
        return len(A)+1
        
