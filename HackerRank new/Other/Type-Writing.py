def callme(operationString, position, result, input3, prevResult):
    if position >= len(operationString):
        return result
    else:
        char = operationString[position]
        if char == 'w':
            prevResult = result
            result = callme(operationString, position +
                            1, result, input3, prevResult)
        elif char == 'd':
            prevResult = result
            result = result[:-input3]
            result = callme(operationString, position +
                            1, result, input3, prevResult)
        elif char == 'u':
            result = callme(operationString, position +
                            1, prevResult, input3, result)
        else:
            result = result + char
            result = callme(operationString, position +
                            1, result, input3, prevResult)
    return result


input1 = input()
input2 = input()
input3 = int(input())
result = callme(input2, 0, input1, input3, "")
print(result)
