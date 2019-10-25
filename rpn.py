"""RPN calculator."""

from colored import fg, bg, attr


def calculate(
        expr,
):
    """Calculate RPN expression."""
    stack = list()
    for token in expr.split():
        if isinstance(token, str) and token in "+-^":
            second_arg = stack.pop()
            first_arg = stack.pop()
            if token == "+":
                stack.append(first_arg + second_arg)
            elif token == "-":
                stack.append(first_arg - second_arg)
            else:
                stack.append(first_arg ** second_arg)
        else:
            stack.append(int(token))

    if len(stack) != 1:
        raise TypeError("malformed input")

    return stack.pop()


def main(
):
    """RPN calculator."""
    while True:
        color = fg("#C0C0C0") + bg("#00005f")
        res = attr("reset")
        calculate(input(f"{color}rpn calc{res} > "))

if __name__ == "__main__":
    main()
