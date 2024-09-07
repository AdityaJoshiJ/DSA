def sum_of_numbers(string):
    numbers = ""
    sum = 0
    for char in string:
        if char.isdigit():
            numbers += char
        else:
            if numbers != "":
                sum += int(numbers)
                numbers = ""
    if numbers != "":
        sum += int(numbers)
    return sum

# Example usage
input_string = input()
result = sum_of_numbers(input_string)
print(result)
