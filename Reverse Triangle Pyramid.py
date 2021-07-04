n =int(input("enter :"))
for i in range(1, n + 1):
    print('-'*(n-i),end="")
    for j in range(i,0,-1):
        print(chr(ord('a') + j - 1),end ="") 
    print()
    
    

