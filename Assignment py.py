a = [[1,2,3,],[4,5,6]]
b = [[9,8,7],[6,9,4]]
for i in a:
    print(i)
for i in b:
    print(b)
for i in range(1):
 for j in range(1):
    result = a[1][j] + b[i][j]
    print("the sum of two matrix is:",result)

list = [1,2,3,4,5,6]
#remove duplicate values
final_list = []
for i in list:
   if i not in final_list:
      final_list.append(i)
print(list)
print(final_list)