def queue():
    if limit != len(queues):
        val = int(input())
        queues.append(val)
        print(queues)
    else:
        print("Full!!!!!")

def dequeue():
    if not queues:
        print("Nothing to dequeue")
    else:
        e = queues.pop(0)
        print("Value Dequeued : ", e)
        print(queues)

limit = int(input())
queues = []
while True:
    print("Enter your choice: 1) add   2)pop   3)exit")
    choice = int(input())
    if choice == 1:
        queue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("enter correct Value")
