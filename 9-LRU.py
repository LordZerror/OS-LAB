capacity = int(input("Enter the number of frames: "))
f, st, fault, pf = [], [], 0, 'No'
s = list(map(int, input("Enter the reference string: ").strip().split()))
print("\nString|Frame ->\t", end='')
for i in range(1, capacity+1):
    print(i, end=' ')
print("Fault")
print("-"*30)
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
            st.append(len(f) - 1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Yes'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'No'
    print("   %d\t\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print(f"\nTotal Requests: {len(s)}\nTotal Page Faults: {fault}\nFault Rate: {str(fault/len(s)*100)[:5]}")