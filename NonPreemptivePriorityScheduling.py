import numpy as np
from tabulate import *

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

# Waiting Time for Each Process
wait_time = processes[0][1]
processes[0].append(0)
for i in processes[1:]:
    i.append(wait_time)
    wait_time = wait_time + i[1]

# Turnaround Time for Each Process
turnaround_time = processes[0][1]
processes[0].append(turnaround_time)
for i in processes[1:]:
    turnaround_time = turnaround_time + i[1]
    i.append(turnaround_time)

ans = [["PROCESS ID", "BURST TIME", "PRIORITY", "WAITING TIME", "TURNAROUND TIME"]] + processes
print("PROCESSES ACCORDING TO THEIR PRIORITY ORDER")
print(tabulate(ans, headers='firstrow', tablefmt="fancy_grid"))

print()
column_sum = np.sum(processes, axis=0)
avg_waiting_time = column_sum[3]/n
avg_turnaround_time = column_sum[4]/n
print("Average Waiting Time of the processes : %.2f" % avg_waiting_time)
print("Average Turnaround Time of the processes : %.2f" % avg_turnaround_time)
