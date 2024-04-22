class Customer:
    def __init__(self, ID, Data):
        self.ID = ID
        self.Data = Data

N = 9

HashTable = [Customer(0, "") for _ in range(N + 1)]

def Hash(Key):
    Address = Key % (N + 1)
    return Address

def Initialize():
    for i in range(0, N + 1):
        HashTable[i].ID = 0
        HashTable[i].Data = ""

def Insert(NewRecord):
    # CASE 1: Hash table is full
    # CASE 2: Address from the hash table is free; insert
    # CASE 3: Address is not free; apply Open Hashing, find the next free slot

    TableFull = False
    Index = Hash(NewRecord.ID)
    Pointer = Index

    while HashTable[Pointer].ID != 0 and not TableFull: # Checking for CASE 2 (If Open Hashing)
        Pointer += 1 # Open Hashing
        if Pointer > N:
            # wrap around
            Pointer = 0

        if Pointer == Index: # Back to the original index
            TableFull = True

    if TableFull:
        print("Cannot insert; table full!")
    else:
        HashTable[Pointer] = NewRecord

def Find(Item):
    TableFull = False
    Index = Hash(Item)
    Pointer = Index

    while HashTable[Pointer].ID != Item and not TableFull:
        Pointer += 1        # Go to the next Slot
        if Pointer > N:     # Go beyond the table boundary
            Pointer = 0     # Wrap around
        
        if Pointer == Index:
            TableFull = True
    
    if HashTable[Pointer].ID == Item:   # If the item is found
        return HashTable[Pointer]
    else:
        return None

# main()
Initialize()

for i in range(1, 6):
    NewCustomer = Customer(None, None)
    NewCustomer.ID = int(input("Enter Customer ID: "))
    NewCustomer.Data = input("Enter Customer Data: ")

SearchID = int(input("Enter Search ID: "))
FindCustomer = Find(SearchID)

if FindCustomer is not None:
    print("ID is", FindCustomer.ID, "Data is", FindCustomer.Data)
else:
    print("Customer not found")