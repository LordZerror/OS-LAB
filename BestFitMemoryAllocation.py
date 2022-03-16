from tabulate import *

print()
print("BEST-FIT MEMORY ALLOCATION TECHNIQUE\n")
n = int(input("Enter the number of memory blocks: "))
print()
blocks = []
for i in range(n):
    print("Enter the memory of block", i+1, ": ", end="")
    x = int(input())
    blocks.append([i+1, x])
    print()

required = int(input("Enter the size of the memory required by the process : "))
fragmentation = []
for i in blocks:
    if i[1] >= required:
        frag = i[1] - required
        i.append(frag)
        fragmentation.append(frag)
    else:
        i.append("Process Size > Block Size")
        fragmentation.append(float('INF'))


best_fit = min(fragmentation)
for i in blocks:
    if type(i[2]) == int and i[2] == best_fit:
        i.append("BEST FIT")
    else:
        i.append("")

print("\nMEMORY BLOCK TABLE\n")
ans = [["BLOCK NUMBER", "SIZE OF MEMORY BLOCK", "FRAGMENTATION", "REMARKS"]] + blocks
print(tabulate(ans, headers='firstrow', tablefmt="fancy_grid"))
