# Your task is to complete this function
# Function should return true/false
def PalinArray(arr):
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
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends