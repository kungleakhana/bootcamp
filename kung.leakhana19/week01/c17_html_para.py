list=[]
while True:
    ch=input("Enter a sentence:")
    list.append(ch)
    if len(list)==1 and ch=="GENERATE":
        list.remove("GENERATE")
        print("Nothing to display.")
        break
    elif ch=="GENERATE":
        list.remove("GENERATE")
        break
for i in list:
        print("<p>"+i+"</p>")