def push():
    if len(stack) == limit:
        element = int(input())
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("stack empty")
    else:
        e = stack.pop()
        print("removed elemnt : ", e)
        print(stack)

limit = int(input("Limit of Stack"))
stack = []
while True:
    print("Enter your choice: 1) push   2)pop   3)exit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("correct operation")

