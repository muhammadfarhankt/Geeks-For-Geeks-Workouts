#User function Template for python3

class Solution:
    def nPr(self, n, r):
        # code here
        npr = 1
        for i in range(1, n+1):
            npr *= i
        if n - r == 0:
            return npr
        for i in range(1, n-r+1):
            npr = npr // i
        return npr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends