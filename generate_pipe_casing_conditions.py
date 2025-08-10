directions = ["down", "east", "north", "south", "up", "west"]

conditions = []

def add_3_permutations(data):
    for i in range(len(data)):
        dir0 = data[i]
        for j in range(i + 1, len(data)):
            dir1 = data[j]
            for k in range(j + 1, len(data)):
                dir2 = data[k]

                conditions.append({dir0: "true", dir1: "true", dir2: "true"})

add_3_permutations(["north", "east", "south", "west"])
add_3_permutations(["north", "up", "south", "down"])
add_3_permutations(["up", "east", "down", "west"])

print(conditions)