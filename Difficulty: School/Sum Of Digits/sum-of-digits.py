#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        # code here
        sum = 0
        while N > 0:
            sum += N % 10
            N = N // 10
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends