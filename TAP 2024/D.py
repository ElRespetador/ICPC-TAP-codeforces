def esposible(a,b,c):
    if (a+b)<=c:
        return True
    elif (a+c)<=b:
        return True
    elif (c+b)<=a:
        return True
    return False

a,b,c= map(int,input().split())
if esposible(a,b,c):
    print("S")
else:
    print("N")
