#%%
string = list("abcd")
M = 3
commands = []
#for loop
commands.append("P x")
commands.append("L")
commands.append("P y")

commands.reverse()

cursor = len(string)

command = commands.pop()

command_list = command.split(" ")
if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

command = commands.pop()

command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

print("".join(string))

#%%
string = list("abc")
M = 9
commands = []

commands.append("L")
commands.append("L")
commands.append("L")
commands.append("L")
commands.append("L")
commands.append("P x")
commands.append("L")
commands.append("B")
commands.append("P y")

commands.reverse()

cursor = len(string)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1
    cursor = max(cursor, 0)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1
    cursor = max(cursor, 0)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "B":
    string[cursor - 1 : cursor] = []


command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

print("".join(string))

string = list("dmih")
M = 11
commands = []
commands.append("B")
commands.append("B")
commands.append("P x")
commands.append("L")
commands.append("B")
commands.append("B")
commands.append("B")
commands.append("P y")
commands.append("D")
commands.append("D")
commands.append("P z")

commands.reverse()

cursor = len(string)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "B":
    string[cursor - 1 : cursor] = []
    cursor -= 1
    cursor = max(0, cursor)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "B":
    string[cursor - 1 : cursor] = []
    cursor -= 1
    cursor = max(0, cursor)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "L":
    cursor -= 1
    cursor = max(cursor, 0)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "B":
    string[cursor - 1 : cursor] = []
    cursor -= 1
    cursor = max(0, cursor)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "B":
    string[cursor - 1 : cursor] = []
    cursor -= 1
    cursor = max(0, cursor)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "B":
    string[cursor - 1 : cursor] = []
    cursor -= 1
    cursor = max(0, cursor)

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "D":
    cursor += 1
    cursor = min(cursor, len(string))
    
command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "D":
    cursor += 1
    cursor = min(cursor, len(string))


command = commands.pop()
command_list = command.split(" ")

if command_list[0] == "P":
    string[cursor:] = command_list[1] + "".join(string[cursor:])
    cursor += len(command_list[1])

#%%
string = list(input())
M = int(input())
commands = []

for _ in range(M):
    c = sys.stdin.readline()
    commands += 

commands.reverse()
cursor = len(string)

for _ in range(M):
    command = commands.pop()
    command_list = command.split(" ")

    if command_list[0] == "P":
        string[cursor:] = command_list[1] + "".join(string[cursor:])
        cursor += len(command_list[1])

    elif command_list[0] == "D":
        cursor += 1
        cursor = min(cursor, len(string))

    elif command_list[0] == "L":
        cursor -= 1
        cursor = max(cursor, 0)

    elif command_list[0] == "B":
        string[cursor - 1 : cursor] = []
        cursor -= 1
        cursor = max(0, cursor)

print("".join(string))

# %%
import sys
num = sys.stdin.readline()