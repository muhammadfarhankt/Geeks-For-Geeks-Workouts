#User function Template for python3

class Solution:
	def is_palindrome(self, n):
		# Code here
		temp = n
		reverse = 0
		while temp > 0) :
		    reverse = (temp % 10) + (reverse * 10)
		    temp = temp // 10
        if (reverse == n):
            return "Yes"
        else:
            return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends