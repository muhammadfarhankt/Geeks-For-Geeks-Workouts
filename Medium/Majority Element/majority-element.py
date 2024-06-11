#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        occurence = {}
        max = N // 2
        val = -1
        for num in A:
            if num in occurence:
                occurence[num] += 1
            else:
                occurence[num] = 1
        #print(occurence)
        for key, val in occurence.items():
            if val > max:
                return key
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends