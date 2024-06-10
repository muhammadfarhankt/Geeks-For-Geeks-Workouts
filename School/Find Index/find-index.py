#User function Template for python3

class Solution:
    def findIndex (self,arr, n, key ):
        #code here.
        output = []
        for i in range(n):
            if arr[i] == key:
                output.append(i)
                break
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == key:
                output.append(i)
                break
        if len(output) != 2:
            return [-1, -1]
        return output
#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends