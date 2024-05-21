data = [1, 2, 3, 4, 5]

print("List menjadi Set: ")
print(f"Before = {data} \t,\t After = {set(data)}\n")

print("Set menjadi List: ")
print(f"Before = {set(data)} \t,\t After = {list(set(data))}\n")

print("Tuple menjadi Set: ")
print(f"Before = {tuple(data)} \t,\t After = {set(tuple(data))}\n")

print("Set menjadi Tuple: ")
print(f"Before = {set(data)} \t,\t After = {tuple(set(data))}\n")