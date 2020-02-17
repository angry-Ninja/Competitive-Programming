for p in range(int(input())):
    s=input()
    k,count=[0,0]
    for i in s:
        if i=="/":
            count+=1
        else:
            count-=1
        if count<0:
            print("Irregular since Childhood.")
            k=1
            break
    if k==0:
        print("Regular since Childhood.")
