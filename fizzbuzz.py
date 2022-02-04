no = input("Enter a number")
no = int(no)
if no%3==0 and no%5==0:
    print("fizzbuzz")
elif no%3==0:
    print("fizz")
elif no%5==0:
    print("buzz")
else:
    print(no)