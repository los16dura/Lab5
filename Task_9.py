#9
A=[0]*100
N = int(input())
for i in range(N):
    A[i] = int(input())
k = int(input())
max = sum(A[0:k])
for i in range(N):
    if max<(max-A[i]+A[i+k]):
        max=max-A[i]+A[i+k]
        print('max=',max)
print(max)