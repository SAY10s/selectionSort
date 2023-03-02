tab = [2, 1, 3, 7, 6, 9, 4, 2, 0]
print(tab)

i = 0
while i < len(tab) - 1:
    minIndex = i
    j = i + 1
    while j < len(tab):
        if tab[j] < tab[minIndex]:
            minIndex = j
        j += 1
    tab[i], tab[minIndex] = tab[minIndex], tab[i]
    i += 1

print(tab)