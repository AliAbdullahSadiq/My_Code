# DECLARE Queue[0:49] of Type String
# DECLARE HeadPointer of Type Integer
# DECLARE TailPointer of Type Integer
global Queue
global HeadPointer
global TailPointer

Queue = [""]*50
HeadPointer = -1
TailPointer = 0

def Enqueue(Insert):
    global Queue , HeadPointer, TailPointer
    
    if TailPointer == 50:
        print("Cannot insert, queue is full")
    else:
        Queue[TailPointer] = Insert
        TailPointer += 1

def Dequeue():
    global Queue , HeadPointer, TailPointer

    if TailPointer == HeadPointer:
        print("Queue is empty, nothing to dequeue")
        return "Empty"
    else:
        temp = Queue[HeadPointer]
        HeadPointer += 1
        
        return temp

def ReadData():
    global Queue

    try:
        File = open("QueueData.txt", 'r')
        line = File.readline().strip()
        i = 0
        while line != '':
            Enqueue(line)
            line = File.readline().strip()
        File.close()
    except IOError:
        print("File does not exist")

# Type RecordData
#   ID : string
#   Total : integer
class RecordData:
    def __init__(self, ID, Total):
        self.ID = ID
        self.Total = Total

global Records
global NumberRecords
Records = []
for i in range(50):
    Records.append(RecordData('', 0))
NumberRecords = 0

def TotalData():
    global NumberRecords, Records
    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for X in range(NumberRecords):
            if Records[X].ID == DataAccessed:
                Records[X].Total += 1
                Flag = True

    if not Flag:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

def OutputRecords():
    global NumberRecords, Records
    for i in range(NumberRecords):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")

# Enqueue("a")
# print(Dequeue())
# ReadData()
# print(Queue)

ReadData()
while HeadPointer != TailPointer:
    TotalData()
OutputRecords()
