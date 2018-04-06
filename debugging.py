#write a sample program to error and debugging
n=int(input('enter the value of n '))
l=[1,2,0,3]
for i in range(len(l)):
    while True:
        try:
            c=n/l[i]
            print(c)
            break
        except ZeroDivisionError:
            print('the n value shoud not zero')
            l[i]=int(input('enter the value of element '))
