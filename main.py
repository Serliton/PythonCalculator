def main(user_input: str):
    operatorIndx = None
    operator = None

    for indx,s in enumerate(user_input):
        match s:
            case "+":
                operatorIndx = indx
                operator = s
            case "-":
                operatorIndx = indx
                operator = s
            case "*":
                operatorIndx = indx
                operator = s
            case "/":
                operatorIndx = indx
                operator = s


    if operatorIndx == None:
        raise Exception("Cтрока не является математической операцией")

    try:
        firstOperand = int(user_input[:operatorIndx])
        secondOperand = int(user_input[operatorIndx + 1:])
    except:
        raise Exception("Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

    if (1 <= firstOperand <= 10) and (1 <= secondOperand <= 10):
        match operator:
            case "+":
                return str(firstOperand + secondOperand)
            case "-":
                return str(firstOperand - secondOperand)
            case "*":
                return str(firstOperand * secondOperand)
            case "/":
                return str(firstOperand // secondOperand)
    else:
        raise Exception("Операнды должны находиться в диапазоне от 1 до 10")


print(main("1 + 2"))
# print(main("1"))
# print(main("1 + 2 1"))
# print(main("1 + 2 + 3"))
