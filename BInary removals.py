n=int(input())
for i in range(n):
    l=input()
    a=l.find('11')
    b=l.rfind('00')

    if(a<b and a!=-1 and b!=-1):
        print("NO")
    else:
        print("YES")
