def max_coins(N, M, X, Y):
    # Create a 2D array to represent the board and initialize all cells to 0
    board = [[0] * M for _ in range(N)]

    # Function to check if a cell is valid to place coins
    def is_valid(i, j):
        if i >= 0 and i < N and j >= 0 and j < M:
            return True
        return False

    # Iterate through each cell in the board
    for i in range(N):
        for j in range(M):
            # Check the neighbors of the current cell
            neighbors_sum = 0
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if is_valid(ni, nj):
                    neighbors_sum += board[ni][nj]

            # Calculate the maximum number of coins that can be placed in the current cell
            max_coins_in_cell = min(X, Y - neighbors_sum)
            # Ensure non-negative value
            max_coins_in_cell = max(0, max_coins_in_cell)

            # Place the maximum number of coins in the current cell
            board[i][j] = max_coins_in_cell

    # Calculate the total number of coins on the board
    total_coins = sum(sum(row) for row in board)

    return total_coins


n, m, x, y = map(int, input().split())

print(max_coins(n, m, x, y))
