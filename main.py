userInput = input("Введите арифметическое выражение с двумя операндами.\nИспользуйте натуральные числа от 1 до 10:\n")

operatorIndx = None
operator = None
firstOperand = None
secondOperand = None


for indx,s in enumerate(userInput):
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
    firstOperand = int(userInput[0:operatorIndx])
    secondOperand = int(userInput[operatorIndx + 1:])
except:
    raise Exception("Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")


match operator:
    case "+":
        print(firstOperand + secondOperand)
    case "-":
        print(firstOperand - secondOperand)
    case "*":
        print(firstOperand * secondOperand)
    case "/":
        print(firstOperand // secondOperand)
