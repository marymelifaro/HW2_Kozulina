def adding(a, b):
    return(a+b)


def diff(a, b):
    pass


def mult(a, b):
    pass


def division(a, b):
    pass


def main():
    expression = input().split()
    a = int(expression[0])
    oper = expression[1]
    b = int(expression[2])
    if oper == '+':
        print(adding(a, b))
    if oper == '-':
        print(diff(a, b))
    if oper == '*':
        print(mult(a, b))
    else:
        print(division(a, b))


main()
