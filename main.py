# pierwsze
# T = [2, 1, 3, 7, 6, 9, 4, 2, 0, ]

#drugie
T = ["b", "a", "k"]
print(T)

for i in range(1, len(T)):
    value = T[i]
    start, end = 0, i-1
    while start <= end:
        mid = (start + end) // 2
        if T[mid] <= value:
            start = mid + 1
        else:
            end = mid - 1
    for j in range(i-1, start-1, -1):
        T[j+1] = T[j]
    T[start] = value

print(T)