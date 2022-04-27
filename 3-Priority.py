import pandas as pd

print()
print("NON PREEMPTIVE PRIORITY SCHEDULING ALGORITHM\n")
print("Here, lower the priority number, higher is the priority\n")
n = int(input("Enter the number of processes: "))
print()
processes = []
for i in range(n):
    print("Enter the burst time of process", i + 1, ": ", end="")
    burst_time = int(input())
    print("Enter the priority of process", i + 1, ": ", end="")
    priority = int(input())
    print()
    process = [i + 1, burst_time, priority]
    processes.append(process)

processes = sorted(processes, key=lambda x: x[2])

waiting, turnaround = [0], []
waiting_time, turnaround_time = 0, 0

for i in range(n-1):
    waiting_time += processes[i][1]
    waiting.append(waiting_time)

for i in range(n):
    turnaround_time += processes[i][1]
    turnaround.append(turnaround_time)

for i in range(n):
    processes[i].append(waiting[i])
    processes[i].append(turnaround[i])

print(pd.DataFrame(processes, columns=['Process Number', 'Burst Time', 'Priority', 'Waiting Time', 'Turnaround Time']))
print(f'''
Average Waiting Time : {sum(waiting)/n:.2f}
Average Turnaround Time : {sum(turnaround)/n:.2f}
''')

