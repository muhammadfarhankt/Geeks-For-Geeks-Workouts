# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    for num in arr:
        if Palindrome(num) == False :
            return False
    return True

def Palindrome(n):
    temp = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n = n // 10
    # print(temp)
    if temp == reverse:
        return True
    else:
        return False

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends