#7-норм задача,жаль,что это последняя,что я успела
m = 0
A = [0,0,0,0,0,0,0,0,0,0]
s = 0
for i in range(10):
    A[i]=int(input())
    if i>=1:
        if A[i-1] == 2 and A[i] != 2 :
                 s=s-2
                 m=m-1
    s=s+A[i]
    #print(s)
    m=m+1
    #print(m)
f = s/m
#print(f)
t = int(f)
print(t)
