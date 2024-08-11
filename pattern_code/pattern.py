def print_pattern(n):

 if n>1:
     return "ValidInput"
    
 else :
    return ("Enter greater number");
    
    print(" " *(n-1) + "*")
    print(" " * (n-2) + "* 1 *")
    print("*" * (2 * n + 1))

print()
print(print_pattern(5))


