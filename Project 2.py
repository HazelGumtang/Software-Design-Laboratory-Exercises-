def move(n,x,y):
    print("Move from "+x+" to "+y)
def Hanoi(x,y,z,n):
    if n==1:
        move(n,x,z)
    else:
        Hanoi(x,z,y,n-1)
        move(n,x,z)
        Hanoi(y,x,z,n-1)
Hanoi('a','b','c',4)