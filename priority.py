from queue import Queue
from tabulate import tabulate

def priority_scheduling(n, teacher_queue, student_queue):
    wait_time = [0] * n         
    turnaround_time = [0] * n   
    remaining_time = [0] * n    
    completed = 0               
    t = 0                       
    priority_queue = []         

    
    for i in range(n):
        if not teacher_queue.empty():
            process_name, burst_time = teacher_queue.get()
            priority_queue.append([i, burst_time, process_name, "Teacher"])
        elif not student_queue.empty():
            process_name, burst_time = student_queue.get()
            priority_queue.append([i, burst_time, process_name, "Student"])


    priority_queue.sort(key=lambda x: (x[0], x[3]))

   
    for i in range(n):
        process_name = priority_queue[i][2]
        burst_time = priority_queue[i][1]
        remaining_time[i] = burst_time

        
        wait_time[i] = t - priority_queue[i][0]
        if wait_time[i] < 0:
            wait_time[i] = 0

   
        t += burst_time
        completed += 1

      
        turnaround_time[i] = t

 
    avg_wait_time = sum(wait_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

  
    results = []
    for i in range(n):
        process_name = priority_queue[i][2]
        burst_time = priority_queue[i][1]
        turnaround = turnaround_time[i]
        waiting = wait_time[i]
        results.append([process_name, burst_time, turnaround, waiting])

    print(tabulate(results, headers=["Process", "Burst Time", "Turnaround Time", "Waiting Time"]))
    print("Average waiting time:", avg_wait_time)
    print("Average turnaround time:", avg_turnaround_time)


n = int(input("Enter the number of processes: "))

teacher_queue = Queue()
student_queue = Queue()


for i in range(n):
    process_name = "P{}".format(i+1)
    burst_time = int(input("Enter burst time for process {}: ".format(process_name)))
    process_type = input("Enter process type for process {} (Teacher/Student): ".format(process_name))
    if process_type.lower() == "teacher":
        teacher_queue.put((process_name, burst_time))
    elif process_type.lower() == "student":
        student_queue.put((process_name, burst_time))


priority_scheduling(n, teacher_queue, student_queue)
