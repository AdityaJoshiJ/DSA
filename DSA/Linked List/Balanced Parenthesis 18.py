def is_balanced(n):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_mapping = {')': '(', ']': '[', '}': '{'}

    for i in n:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            if not stack or stack.pop() != bracket_mapping[i]:
                return False

    return True


n = input().strip()
print(is_balanced(n))
