4
A = [1,2,3,4,2]

i = 0
t = int(input())
for i in range(t):
    s = A.pop()
    A.insert(len(A)-s,s)
    print(A)

