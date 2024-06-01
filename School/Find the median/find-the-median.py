#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		size = len(v)
		if size % 2 == 1 :
		    return v[(size//2)]
		else :
		    return (v[(size//2)] + v[(size//2)-1]) // 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends