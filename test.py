# #1
# A = []
# for i in range(int(input())):
#     A.append(int(input()))
# # for i in range(len(A)):
# #1-1
# print(A[1::2])
# #1-2
# print(max(A))
# #1-3
# print(A[::-1])
# i=0
#
# #2
#
#
# #2-1
# while i < (len(A)-1):
#     A[i], A[i + 1] = A[i + 1], A[i]
#     i+=2
# print(A)
#
#
# #2-2
#
# i=0
# for i in range(len(A)-1):
#      #a=A[0]
#      a = A.pop(0)
#      A.append(a)
# print(A)
#
# #2-3
# i= 0
# for i in range(len(A)):
#  if  A.count(A[i])==1:
#      print(A[i],end=' ')
#
# print()
#
A = [1, 3, 2, 32,32]
# #2-4
# max=1
# max_i=1
# for i in range(len(A)):
#     if A.count(A[i])> max:
#         max=A.count(A[i])
#         max_i=i
# print(A[max_i])


# #3
# k = 0
# for i in range(len(A)):
#     if k >= len(A):
#         break
#     #print('k=',k)
#     print(A[i],end=' ')
#     k=k+1
#     if k >= len(A):
#         break
#
#     print(A[len(A)-i-1],end=' ')
#     k = k + 1



#4
# A = [1,2,3,4,2]
#
# i = 0
# t = int(input())
# for i in range(t):
#     s = A.pop()
#     A.insert(len(A)-s,s)
#     print(A)
#


#5

k=(int (input() ))
n=(int (input() ))
#A[n+1]
for i in range (0, n):
    A[i]=0
for i in range (0,k-1):
    A[i]=1 #заполнил единцами первые K элементов с нулевого до k-1
for i in range (k, n):
    for j in range (i-1, i-k, -1):
        A[i]=A[i]+A[j]
print(A[n])
print(A)