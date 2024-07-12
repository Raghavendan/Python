z=int(input("Enter a Number:"))
if z>1:
    for i in range(2,z):
        if(z%i==0):
            print(z,'Not a prime number')
            break
    else:
        print(z,'Prime Number')
else:
    print(z,'Not prime number')
