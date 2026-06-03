def hanoi_solver(n):
    # Initialize rods
    source = list(range(n, 0, -1))  # [n, ..., 1]
    auxiliary = []
    target = []

    moves = []

    # Helper to record current state
    def record():
        moves.append(f"{source} {auxiliary} {target}")

    # Recursive Hanoi function
    def solve(num, src, aux, dest):
        if num == 1:
            dest.append(src.pop())
            record()
        else:
            solve(num - 1, src, dest, aux)
            dest.append(src.pop())
            record()
            solve(num - 1, aux, src, dest)

    # Record initial state
    record()

    # Solve the puzzle
    solve(n, source, auxiliary, target)

    # Return all moves as a string
    return "\n".join(moves)

print(hanoi_solver(3))
