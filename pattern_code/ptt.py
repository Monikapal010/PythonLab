def print_pattern(n):
   
  
   for i in range(n):
    for j in range(n-i):
     print('   *   ',end=" ")
     
    print()

print_pattern(5)
