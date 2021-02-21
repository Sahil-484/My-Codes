x=[1,3,4,5,6,8,9,2,7]
n=len(x)
for i in range(0,n):
    for j in range(i+1,n):
        if x[i]>x[j]:
            y=x[i]
            x[i]=x[j]
            x[j]=y
print(x)
        

           
