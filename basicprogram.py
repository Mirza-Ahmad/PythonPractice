print('Enter any four digit number')
 #Now take input from user
Str=input()
 #The input() function return input as string we will convert into integer
W=int(Str)
C=W%1000
W=W//1000
print(W)
W=C%100
C=C//100
print(C)
C=W%10
W=W//10
print(W)
W=C%1
C=C//1
print(C)

def replacei(x):
    return x.replace("\n","")

list1=['ahmad\n','zaryab\n','ali\n']
result = map(replacei, list1)
print(list(result))

Req_Info=int(input('Note: Before enter a next number the space is mandatory among the numbers \nHow many numbers are required ? : '))
my_list=[Req_Info]
check=my_list=input(' Enter the numbers: ').split()
print(check,"\n",type(check))