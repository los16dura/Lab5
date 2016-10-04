
#3
A = [1, 2, 3, 4, 5]
k = 0
for i in range(len(A)):
    if k >= len(A):
        break
    #print('k=',k)
    print(A[i], end=' ')
    k += 1
    if k >= len(A):
        break

    print(A[len(A)-i-1],end=' ')
    k += 198