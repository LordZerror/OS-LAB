ls = list(map(int, input("\nEnter the sequence : ").split()))
start = int(input("Enter the starting position of the sequence : "))
direction = input("Enter the direction to first move to : ")

right = []
left = []
ans = []

for i in ls:
    if i < start:
        left.append(i)
    else:
        right.append(i)

left.sort()
right.sort()
left.reverse()

if direction.lower() == 'right':
    right_end = int(input("Enter the maximum limit of the disk : "))
    ans = [start] + right + [right_end] + left
if direction.lower() == 'left':
    ans = [start] + left + [0] + right

total = 0
for i in range(len(ans)-1):
    total += abs(ans[i+1] - ans[i])

final = list(map(str, ans))
print(f'''
Seek Sequence : {" --> ".join(final)}

Total number of Seek Operations : {total}''')