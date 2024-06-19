#User function Template for python3

class Solution:
	def DiagonalSum(self, matrix):
		# Code here
		n = len(matrix)
		sum = 0
		for i in range(0, n):
		    sum += matrix[i][i] + matrix[i][n-i-1]
		return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.DiagonalSum(matrix)
		print(ans)
# } Driver Code Ends