#5

k=(int (input() ))
n=(int (input() ))

#A[n+1]
A=[0]*(n+1) #задаю массив из n+1 элементов (если надо посчитать 6, то в массиве 7 элементов от 0 до 6)
#print(A)
for i in range (0, k): #заполняю первые k Элементов единицами. не понимаю почему цикл до k, а не до k-1
    A[i]=1
#print (A)
#print (A[0])
#print ("*********")

for i in range (k, n+1):  #считаю оствшиеся элементы до n-ого
    for j in range (i-1, i-k-1, -1):
        A[i]=A[i]+A[j]
    #print(i,A[i])
print(A[n])  #вывожу n-ный элемент
print(A)     #вывожу весь массив
#прога не работает, если задаешь n<k


