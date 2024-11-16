import math

val1 = input("Value One: ")
print(val1)

mathSymbol = input("Symbol: ")
print(val1, mathSymbol)

val2 = input("Value Two: ")

# Checks if any of the values have Pi in them.
if val1 == "pi":
    val1 = math.pi

elif val2 == "pi":
    val2 = math.pi

# Checks what symbol was inputted and calculates the answer.
if mathSymbol == "+":
    answer = float(val1) + float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)

elif mathSymbol == "-":
    answer = float(val1) - float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)

elif mathSymbol == "*":
    answer = float(val1) * float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)

elif mathSymbol == "/":
    answer = float(val1) / float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)