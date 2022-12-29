


def calculator(message):
    global res
    numbers = re.split(r"[+|\-|*|/]", message.text)
    oper = [i for i in re.split(r"\d+", message.text) if i != '.' and i != '' and i != ' ']
    x = float(numbers[0])
    y = float(numbers[1])
    if oper[0] == '+':
        res = oc.summa(x, y)
    elif oper[0] == '-':
        res = oc.sub(x, y)
    elif oper[0] == '*':
        res = oc.mul(x, y)
    elif oper[0] == '/':
        res = oc.div(x, y)

