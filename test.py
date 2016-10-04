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
#A = [1, 3, 2, 32,32]
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
#
# k=(int (input() ))
# n=(int (input() ))
#
# #A[n+1]
# A=[0]*(n+1) #задаю массив из n+1 элементов (если надо посчитать 6, то в массиве 7 элементов от 0 до 6)
# #print(A)
# for i in range (0, k): #заполняю первые k Элементов единицами. не понимаю почему цикл до k, а не до k-1
#     A[i]=1
# #print (A)
# #print (A[0])
# #print ("*********")
#
# for i in range (k, n+1):  #считаю оствшиеся элементы до n-ого
#     for j in range (i-1, i-k-1, -1):
#         A[i]=A[i]+A[j]
#     #print(i,A[i])
# print(A[n])  #вывожу n-ный элемент
# print(A)     #вывожу весь массив
# #прога не работает, если задаешь n<k
#



# #6
# A = [6,1,9,2,3,4,8]
# i = 0
# me = 0 #предыдущий максимум
# j =0
# max = max(A)+1 #это просто максимум,мы его берём таким большим,чтобы  me был больши при первом сравнении с предыдущим максимум
# while j <= (len(A)//2):#ищем "средний" по счёту максимум,тоесть как раз медиану
#     me = max
#     max = -1
#     #print('-----')
#     for i in range(len(A)):#максмум ищем по обычному алгоритму,а не ленивой функцией питона)
#
#         if A[i] > max and me >A[i]:#нахожу максимум но не больший предыдущего максимума
#             max = A[i]
#             #print(max)
#     j = j + 1
# print(me)
# #ой в этой задаче я заыла ,что длина массива вводится,но без разницы же?
#7-норм задача,жаль,что это последняя,что я успела
# m = 0
# A = [0,0,0,0,0,0,0,0,0,0]
# s = 0
# for i in range(10):
#     A[i]=int(input())
#     if i>=1:
#         if A[i-1] == 2 and A[i] != 2 :
#                  s=s-2
#                  m=m-1
#     s=s+A[i]
#     #print(s)
#     m=m+1
#     #print(m)
# f = s/m
# #print(f)
# t = int(f)
# print('His or her mark is ', t)
#
# #8-ой,ваще изи
# A=[]
# B=[]
# N = int(input())
# for i in range(N)
#     A[i] = int(input())
#     B[i] = int(input())
# T = int(input())
# for i in range(N):
#     if T>=A[i]and T<=B[i]:
#         k = k + 1
# print(k)
# #9
# A=[0]*100
# N = int(input())
# for i in range(N):
#     A[i] = int(input())
# k = int(input())
# max = sum(A[0:k])
# for i in range(N):
#     if max<(max-A[i]+A[i+k]):
#         max=max-A[i]+A[i+k]
#         print('max=',max)
# print(max)

#10 што та ни работает
a = [[0] * 20]*20
N = int(input())
a[0][0] = 1
a[1][0] = 1
a[1][1] = 1
for i in range (2,N):
    a[i][0]=1
    for j in range (0,i+1):
       if j==i:
            a[i][j]=1
       else:
            a[i][j]=a[i-1][j-1]+a[i-1][j]
if N<10:
    k=4
else:
    k=5
for i in range(0,N):
    print((N-i+1+((k // 2)-1)*(N-i)))
    for j in range(0,i):
     print(a[i][j],k)

#10попытка номер два









