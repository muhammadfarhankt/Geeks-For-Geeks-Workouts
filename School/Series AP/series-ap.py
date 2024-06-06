
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        return (a1 + (a2-a1) * (n-1))



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a1 = int(input())
        
        
        a2 = int(input())
        
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthTermOfAP(a1, a2, n)
        
        print(res)
        

# } Driver Code Ends