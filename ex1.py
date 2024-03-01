import sys

def calculate_expression(expr):
    def parse_tokens(input_expr):
        expr_tokens = input_expr.replace('(', ' ( ').replace(')', ' ) ').split()
        return expr_tokens

    def perform_operations(tokens):
        stack = []
        for token in tokens:
            if token == ')':
                sub_expr = []
                while stack and stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()
                sub_expr = sub_expr[::-1]
                operator, operand1, operand2 = sub_expr[0], int(sub_expr[1]), int(sub_expr[2])
                if operator == '+':
                    stack.append(operand1 + operand2)
                elif operator == '-':
                    stack.append(operand1 - operand2)
                elif operator == '*':
                    stack.append(operand1 * operand2)
                elif operator == '/':
                    stack.append(operand1 / operand2) 
            else:
                stack.append(token)
        return stack[0]

    expr_tokens = parse_tokens(expr)
    result = perform_operations(expr_tokens)
    print(result)

if __name__ == "__main__":
    user_input_expr = sys.argv[1]
    calculate_expression(user_input_expr)


