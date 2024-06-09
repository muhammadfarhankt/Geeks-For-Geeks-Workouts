class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	arrSet = set()
    	duplicateSet = set()
    	for i in arr:
    	    if i in arrSet:
    	        duplicateSet.add(i)
    	    else:
    	        arrSet.add(i)
    	if duplicateSet:
    	    return sorted(list(duplicateSet))
    	else:
    	    return [-1]


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends