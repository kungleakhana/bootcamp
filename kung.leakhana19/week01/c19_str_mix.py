a=input("Enter a word: ")
if len(a)==0:
    print("0000")
elif len(a)==1:
    print(a*4)
elif len(a)==2:
    print(a*2)
else:
    string1=a[1::-1]
    string2=a[-1:-3:-1]
    print(string1+string2)