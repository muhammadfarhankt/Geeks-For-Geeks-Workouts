class Solution:
    def findSum(self,A,N): 
        #code here
        minm = 0
        maxm = 0
        if N == 1:
            return 2 * A[0]
        if A[0] > A[1]:
            minm = A[1]
            maxm = A[0]
        else:
            minm = A[0]
            maxm = A[1]
        for i in range(2, N):
            if A[i] > maxm:
                maxm = A[i]
            if A[i] < minm:
                minm = A[i]
        return minm + maxm



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends