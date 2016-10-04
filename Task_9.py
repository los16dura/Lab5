#9
A = [0]*100
N = int(input())
for i in range(N):
    A[i] = int(input())
k = int(input())
ma = sum(A[0:k])
for i in range(N):
    if ma < (ma-A[i]+A[i+k]):
        ma = ma-A[i]+A[i+k]
        #print('max=',ma)
print(ma)