import numpy as np

i = 0
j = 0

# Лісти [] можна змінювати
list = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 10, 11, 12], 
                 [13, 14, 15, 16]])
print(type(list))
print(list[i][j])

# Можна змінити значення
list[i][j] = 0
print(list[i][j])

# Тьюпл () масиви фіксовані
tuple = np.array(([-1, 2, 0, 4],
                  [4, -0.5, 6, 0],
                  [2.6, 0, 7, 8],
                  [3, -7, 4, 2.0]))
print(type(tuple))
print(tuple[i][j])

# Можна змінити значення
tuple[i] = [0, 0, 0, 0]
print(tuple[i])

# =======
fruits = ['apples', 'bananas', 'grapes', 'mangoes']
print(type(fruits))
# <class 'list'>
print(fruits)
fruits[0] = 'oranges'
print(fruits)

fruits = ('apples', 'bananas', 'grapes', 'mangoes')
print(type(fruits))
# <class 'tuple'>
print(fruits)
fruits[0] = 'oranges'
# TypeError: 'tuple' object does not support item assignment
print(fruits)