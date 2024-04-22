Jobs = [[0]*2 for i in range(100)]

global NumberOfJobs
NumberOfJobs = 0

def Initialize():
    global NumberOfJobs
    for i in range(100):
        for j in range(2):
            Jobs[i][j] = -1
    
    NumberOfJobs = 0

def AddJob(JobNum, priority, Jobs):
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Jobs are full")
        return 'Not Added'
    else:
        Jobs[NumberOfJobs][0] = JobNum
        Jobs[NumberOfJobs][1] = priority


# Initialize()
# print(Jobs)