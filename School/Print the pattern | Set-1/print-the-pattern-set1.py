def printPat(n):
    #Code here
    for i in range(n, 0, -1) :
        for j in range(n, 0, -1) :
            for _ in range(i) :
                print(j, end = ' ')
        print('$', end = '')
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        printPat(n)
        print()

# } Driver Code Ends