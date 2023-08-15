
signal = 0, 5, 10, 20, 50, 75, 100;

# debug
print(len(signal));
r = range(len(signal));
print(r);

for element in signal:
    print(element);

for element in r:
    print(element);

#len повертає просто число
#range повертає ітерований інтервал від 0 до ...
for i in range(len(signal)): 
    print(i);