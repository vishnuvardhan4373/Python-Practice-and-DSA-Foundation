def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
                
    return stack[0]

print(evaluate_postfix("2 3 +"))       
print(evaluate_postfix("5 2 + 3 *"))   
print(evaluate_postfix("8 2 /"))       