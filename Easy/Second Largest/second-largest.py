#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		large = arr[0]
		second = -1
# 		if arr[0] > arr[1] :
# 		    large = arr[0]
# 		    second = arr[1]
#         elif arr[0] < arr[1] :
#             large = arr[1]
# 		    second = arr[0]
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
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends