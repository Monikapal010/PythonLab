def print_pattern():
    l = int(input("Enter the value of l: "))
    n = l + 2  
    
    
    for i in range(n - 1):
        print(" " * (n - i - 1), end="")
        print("+", end="")
        print(" " * (2 * i - 1) + "+" *(i != 0) )
        print()  

    
    for i in range(n - 4, -1, -1):
        print(" " *(n - i - 1), end=" ")
        print("-",end="")
        print(" " *(2 * i - 1)+" " +" - " +" ")
        print()
       

    print(" " * (n - 1) + "-")

print_pattern()

