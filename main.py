import random

# pierwsze
# T = [2, 1, 3, 7, 6, 9, 4, 2, 0, ]

#drugie
# T = ["b", "a", "k"]

#trzecie
T = []
for x in range(10):
    T.append(random.randint(-10, 100))
print(T)
#koniec trzeciego

i = 0
while i < len(T) - 1:
    minIndex = i
    j = i + 1
    while j < len(T):
        if T[j] < T[minIndex]:
            minIndex = j
        j += 1
    T[i], T[minIndex] = T[minIndex], T[i]
    i += 1

print(T)