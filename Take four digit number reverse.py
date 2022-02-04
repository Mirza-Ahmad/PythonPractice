#Take four digit number form user and print the reverse of this number
r1=input("Enter a four digit number: ")
rev=int(r1)
length=len(r1)
x=0
while x in range(x, length):
 w=rev%10
 rev=rev//10
 x=x+1
 print(w, end=" ")