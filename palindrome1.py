def ispalindrome():
  n=int(input("enter the value:"))
  s=str(n)
  rev=s[::-1]
  
  if s==rev:
   print("The no. is palindrome")
   
  else:
   print("The no. is not palindrome")
   
ispalindrome()
