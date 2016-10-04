#2
A=[1,2,3,4,5]
i = 0
#2-1
while i < (len(A)-1):
    A[i], A[i + 1] = A[i + 1], A[i]
    i += 2
print(A)


#2-2

i=0
for i in range(len(A)-1):
     #a=A[0]
     a = A.pop(0)
     A.append(a)
print(A)

#2-3
i= 0
for i in range(len(A)):
 if  A.count(A[i])==1:
     print(A[i],end=' ')

print()

A = [1, 3, 2, 32,32]
#2-4
max = 1
max_i=1
for i in range(len(A)):
    if A.count(A[i])> max:
        max=A.count(A[i])
        max_i=i
print(A[max_i])
