def calculate(expression)->int:
    print(expression)

    def convert(str):
        lst = [x for x in list(str) if x != ' ']
        out = ""
        stack = []
        for x in lst:
            if x.isdigit():
                out += x
            elif x == '(':
                stack.append(x)
            elif x == ')':
                while True:
                    t = stack.pop()
                    if t != '(':
                        out += t
                    else:
                        break

            else:
                if stack != [] and stack[-1] != '(':
                    out += stack.pop()
                stack.append(x)
        for x in stack:
            out += x
        return out


    def polska(srt):
        import operator
        OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        stack = []
        lst = list(srt)
        for i in srt:
            if i.isdigit():
                stack.append(i)
                lst.remove(i)
            else:
                cnt1, cnt2 = stack.pop(), stack.pop()
                stack.append(OPERATORS[i](int(cnt2), int(cnt1)))
                lst.remove(i)
        return stack.pop()

    polska_str = convert(expression)
    return polska(polska_str)


with open('input.txt', 'r') as reader:
    result = sum([calculate(x) for x in reader.read().split('\n')])

print(result)