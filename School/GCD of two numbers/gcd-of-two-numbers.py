
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if b == 0:
            return a
        return self.gcd(b, a % b)



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends