with open("maze2.txt", "r") as f:
    maze = [list(line.rstrip("\n")) for line in f]

for row in maze:
    for cell in row:
        print(cell, end="")
    print("\n")

function recognize_path(maze, pos):
    if maze[pos[0]][pos[1]] == "┼":
        return directions["up"], directions["down"], directions["left"], directions["right"]
    if maze[pos[0]][pos[1]] == "─":
        return directions["left"], directions["right"]
    if maze[pos[0]][pos[1]] == "│":
        return directions["up"], directions["down"]
    return ()