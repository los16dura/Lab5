#8-ой,ваще изи
A = []
B = []
k = 0
N = int(input())
for i in range(N):
    A[i] = int(input())
    B[i] = int(input())
T = int(input())
for i in range(N):
    if (T >= A[i]) and (T <= B[i]):
        k += 1
print(k)