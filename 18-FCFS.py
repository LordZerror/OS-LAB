print()

ls = list(map(int, input("Enter the sequence : ").split()))
head = int(input("Enter the starting position of the sequence : "))

final = [head] + ls
total = 0

for i in range(len(final) - 1):
    total += abs(final[i+1] - final[i])

final = list(map(str, final))

print(f"\nTotal seek count : {total}")
print("Sequence of operation : ", end="")
print(" -> ".join(final))