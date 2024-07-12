#Normal Star
for i in range(5):
    x='* '
    x=x*i
    print(f'{x: ^10}')
print("--------Normal--------")
#Reverse Star
for i in range(5):
    x='* '
    x=x*(5-i)
    print(f'{x: ^10}') 
print("--------Reverse--------")


#Left Pyramid
for i in range(5):
    x='* '
    x=x*i
    print(f'{x: <10}')
print("--------left--------")


#Right Pyramid
for i in range(5):
    x='* '
    x=x*i
    print(f'{x: >10}')
print("--------Right--------")
