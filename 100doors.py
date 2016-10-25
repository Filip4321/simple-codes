doors = [False] * 100
for i in range(100):
    for j in range(i, 100, i + 1):
        doors[j] = not doors[j]

print("The following doors are open:")

for index, door_state in enumerate(doors):
    if door_state:
        print((format(index + 1)), end = ", ")
