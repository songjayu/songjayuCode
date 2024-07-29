import sys

case = int(sys.stdin.readline())
queue = []

for _ in range(case):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        command = command.strip("push")
        queue.append(int(command))
    if command == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    if command == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    if command == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    if command == "size":
        print(len(queue))
    if command == "pop":
        if not queue:
            print(-1)
        else:
            poppedNum = queue[0]
            queue.pop(0)
            print(poppedNum)