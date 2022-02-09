lst = open("Week6/pltr.txt").readlines()

print(lst)

for i in range(len(lst)):
    lst[i] = float(lst[i])
print(lst)


total = 0
for j in lst:
    total += j
print("\nAverage: " + str(total/len(lst)))