# Інколи при ітерації необхідно отримати не тільки обєкт,
# але і його номер.

msg = ['a', 'b', 'c'];

for position, object in enumerate(msg):
    print(position, object);