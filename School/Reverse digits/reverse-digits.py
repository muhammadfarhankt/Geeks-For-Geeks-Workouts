#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		# Code here
		reverse = 0
		while n > 0 :
		    reverse = (n % 10) + (reverse * 10)
		    n = n // 10
        return reverse

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends