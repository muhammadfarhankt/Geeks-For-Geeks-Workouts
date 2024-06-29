#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        idxA = [0] * 26
        idxB = [0] * 26
        for char in a:
            idx = ord(char) - ord('a')
            idxA[idx] += 1
        for char in b:
            idx = ord(char) - ord('a')
            idxB[idx] += 1
        # print(idxA)
        # print(idxB)
        return idxA == idxB

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends