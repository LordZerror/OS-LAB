print()
ls = list(map(int, input("Enter the sequence : ").split()))
start = int(input("Enter the starting position of the sequence : "))

head = start
total, count = 0, 0
sequence, temp = [start], ls.copy()

while count < len(ls):
    ans = 0
    minimum = float('INF')
    for i in range(len(temp)):
        if abs(head - temp[i]) < minimum:
            minimum = abs(head - temp[i])
            ans = i
    total += minimum
    head = temp[ans]
    temp.pop(ans)
    sequence.append(head)
    count += 1

final = list(map(str, sequence))
print(f'''
Seek Sequence : {" --> ".join(final)}

Total number of Seek Operations : {total}''')