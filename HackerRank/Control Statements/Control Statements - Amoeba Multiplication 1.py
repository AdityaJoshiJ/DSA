def calculate_amoeba_size(month):
    if month <= 0:
        return 0
    elif month == 1:
        return 1
    else:
        previous_size = 0
        current_size = 1
        for _ in range(2, month):
            next_size = previous_size + current_size
            previous_size = current_size
            current_size = next_size
        return current_size


n = int(input())
print(calculate_amoeba_size(n))
