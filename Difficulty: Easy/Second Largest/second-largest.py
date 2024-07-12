#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        large = arr[0]
        second = -1
        n = len(arr)
        for i in range(1, n) :
            if arr[i] > large :
                second = large
                large = arr[i]
            elif arr[i] > second and arr[i] != large:
                second = arr[i]
        return second

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends