rows=int(input("enter a number of rows"))
for i in range(1,rows+1):
   for j in range (1,i+1):
       print(i*j,end='')
   print()
