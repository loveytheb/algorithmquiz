input_data= input()

A, B = input_data.split()

A = int(A)
B = int(B)

if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')