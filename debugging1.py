def area(l,b):
    if l==0:
        raise Exception('the length cannot be zero')
    elif b==0:
        raise Exception('the breadth cannot be zero')
    else:
        area=l*b
        print('the area of a rectangle is ',area)
l=int(input('enter the value of l '))
b=int(input('enter the value of b '))
while True:
    try:
        area(l,b)
        break
    except Exception as err:
        print('Debugging Error :',err)
        if 'length' in str(err):
            l=int(input('enter the value of l'))
        if 'breadth' in str(err):
            b=int(input('enter the value of b'))
    
