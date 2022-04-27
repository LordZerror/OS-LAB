import pandas as pd

print("FIRST FIT MEMORY ALLOCATION")
print("-"*45)
n = int(input("\nEnter the number of blocks : "))
ls = []
print()
for i in range(n):
    ls.append(int(input(f"Enter the size of block {i+1} : ")))

block_size = int(input("\nEnter the size of the block : "))
ans = [[i+1, ls[i]] for i in range(n)]

for i in range(n):
    if ls[i] >= block_size:
        ans[i].append("First Fit")
        break

# print(ans)
print()
print(pd.DataFrame(ans, columns=['Block Number', 'Block Size', 'Remark']))