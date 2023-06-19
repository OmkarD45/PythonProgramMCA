'''
Write a program to print following pattern
	    1
      2 4 6
   2 4 6 8 10
 2 4 6 8 10 12 14

'''
n=5
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end='')
    for j in range (1,i+1):
        print(j*2,end=' ')
    print()