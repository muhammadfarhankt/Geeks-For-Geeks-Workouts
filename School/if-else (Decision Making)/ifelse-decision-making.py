
class Solution:
    def compareNM(self, n : int, m : int) -> str:
        # code here
        if (n == m):
            return "equal"
        elif (n > m):
            return "greater"
        else :
            return "lesser"
#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        obj = Solution()
        res = obj.compareNM(n, m)
        
        print(res)
        

# } Driver Code Ends