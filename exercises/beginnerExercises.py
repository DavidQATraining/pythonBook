
def helloWorld():
    return "Hello World!"


def assignments():
    hello = "Hello World!"
    return hello


def parameters():
    name = str(input("Enter your name: "))
    return "Hello " + name


def parametersOperators(int1, int2):
    return str(int1) + " + " + str(int2) + " = " + str(int1 + int2)


def conditionals(int3, int4, tOf):
    str1 = ""
    if tOf == "True":
        str1 = str(int3) + " + " + str(int4) + " = " + str(int3+int4)
    elif tOf == "False":
        str1 = str(int3) + " * " + str(int4) + " = " + str(int3*int4)
    return str1


def conditionals2(num1, num2, tOf):
    str1 = ""
    if num1 != 0 and num2 != 0:
        if tOf == "True":
            str1 = (str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
        elif tOf == "False":
            str1 = (str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
    elif num1 == 0:
        str1 = str(num2)
    elif num2 == 0:
        str1 = str(num1)

    return str1


def recusion(num1, num2, tOf):
    str1 = ""
    for i in range(10):
        str1 += conditionals2(num1, num2, tOf)
    return str1


def lists(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    list1 = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
    return list1[0]


def recursionLists(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    list1 = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
    str1 = ""
    for i in range(0, len(list1)-1):
        str1 += str(list1[i]) + ", "

    str1 = str1 + str(list1[9])
    return str1


