def AddBinary(a,b):
 binary_1=int(a,2)
 #binary_1=bin(p)[2:]
 
 binary_2=int(b,2)
 #binary_2=bin(q)[2:]
 
 binary_result = (binary_1 + binary_2)
 
 result=str(bin(binary_result)[2:])
 
 return result
 
print(AddBinary("11","1"))
