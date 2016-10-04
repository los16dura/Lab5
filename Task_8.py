#8-ой,ваще изи
A=[]
B=[]
N = int(input())
for i in range(N):
    A[i] = int(input())
    B[i] = int(input())
T = int(input())
for i in range(N):
    if T>=A[i]and T<=B[i]:
        k = k + 1
print(k)