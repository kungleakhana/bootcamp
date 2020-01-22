a=input("Enter something:")
b=a.replace("","")
c=0
if len(a)==0:
    print("EMPTY")
else:
    for i in a:
        string = (i.upper() + i.lower()*c)
        c +=1
        if c == len(a):
            print(string,end="")
        else:
            print(string,end="-")