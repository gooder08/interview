def balance(string):
    stack = []
    for char in string:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if len(stack) == 0:
                return 'Несбалансированно'
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return 'Несбалансированно'

    return 'Сбалансированно'


print(balance('[([])((([[[]]])))]{()}'))

