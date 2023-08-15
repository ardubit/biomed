import numpy as np

# Лісти [] можна змінювати
list = np.array([[1, 2, 3, 4, 1, 2, 3, 4], 
                 [5, 6, 7, 8, 5, 6, 7, 8]])
# print(type(list))
# print(list[0][0])
print(list)

for i in range(len(list)):
    print(i)
    print(range(len(list)))
    mean = np.mean(list[i])
    print(mean)

    for j in range(len(list[i])):
        print(j)
        print(range(len(list[i])))
        list[i][j] = list[i][j] - mean

print(list)
