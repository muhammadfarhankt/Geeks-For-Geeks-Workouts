#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        sum = 0
        while n > 0 :
            sum += n % 10
            n = n // 10
        # print(sum, end = '')
        rev = 0
        temp = sum
        while temp > 0 :
            rev = rev * 10 + temp % 10
            temp = temp // 10
        if rev == sum :
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends