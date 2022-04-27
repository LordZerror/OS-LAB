import pandas as pd
import tabulate

print("WORST FIT MEMORY ALLOCATION")
print("-"*45)
n = int(input("\nEnter the number of blocks : "))
ls = []
print()
for i in range(n):
    ls.append(int(input(f"Enter the size of block {i+1} : ")))

block_size = int(input("\nEnter the size of the block : "))
fragmentation = []

for i in ls:
    if i < block_size:
        fragmentation.append(-float('INF'))
    else:
        fragmentation.append(i - block_size)

ans = [[i+1, ls[i], fragmentation[i]] for i in range(n)]

for i in range(n):
    if type(fragmentation[i]) == int and fragmentation[i] == max(fragmentation):
        ans[i].append('WORST FIT')
    else:
        ans[i].append('')

# print(ans)

print(pd.DataFrame(ans, columns=['Block Number', 'Block Size', 'Fragmentation', 'Remark']))