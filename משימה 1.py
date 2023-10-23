i=0
nbnum=""
def convertor(num1,m):
    bnum="0"
    m=m-2
    while(m>=0):
        if(2**m<=num1):
            bnum+="1"
            num1-=2**m   
        else:
            bnum+="0"
        m=m-1
    print(bnum)
    return(bnum)


try:
    num1=input("num")
    num1=int(num1)
    m=input("write a num of the memory")
    m=int(m)
    
except ValueError as e:
    print("Invalid value")
if(num1<0):
    print("Invalid value")
else:
    bnum= convertor(num1,m)
    l=list(bnum)
    j=len(l)
    j-=1
    while(j>0):
        if(l[j]=="1"):
            count=j
            j=-1
        else:
            j-=1
            count=-1
    j=0
    if(count!=-1):
        while(j<count):
            if(l[j]=="1"):
                l[j]="0"
            else:
                l[j]="1"
            j+=1
        j=0
        while(j<len(l)):
            nbnum+=l[j]
            j+=1
    print(nbnum)

    


