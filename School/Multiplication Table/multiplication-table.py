#User function Template for python3

class Solution:
    def getTable(self,N):
        # code here
        arr = [N]
        for i in range(2, 11):
            arr.append(N * i)
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends