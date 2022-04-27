import pandas as pd

print()
print("SJF SCHEDULING ALGORITHM\n")
n = int(input("Enter the number of processes: "))
print()
processes = []
burst_times = []
for i in range(n):
    print("Enter the burst time of process", i + 1, ": ", end="")
    burst_time = int(input())
    burst_times.append(burst_time)
    processes.append([i+1, burst_time])

processes = sorted(processes, key=lambda x: x[1])
burst_times.sort()
waiting, turnaround = [0], []
waiting_time, turnaround_time = 0, 0
for i in range(n-1):
    waiting_time += burst_times[i]
    waiting.append(waiting_time)

for i in range(n):
    turnaround_time += processes[i][1]
    turnaround.append(turnaround_time)

for i in range(n):
    processes[i].append(waiting[i])
    processes[i].append(turnaround[i])

print()
print(pd.DataFrame(processes, columns=['Process Number', 'Burst Time', 'Waiting Time', 'Turnaround Time']))
print(f'''
Average Waiting Time : {sum(waiting)/n:.2f}
Average Turnaround Time : {sum(turnaround)/n:.2f}
''')