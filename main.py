import math

val1 = input("Value One: ")
print(val1)

mathSymbol = input("Symbol: ")

# Checks if the math symbol is a word
if str.lower(mathSymbol) == "plus":
    mathSymbol = "+"

elif str.lower(mathSymbol) == "minus":
    mathSymbol = "-"

elif str.lower(mathSymbol) == "times":
    mathSymbol = "*"

elif str.lower(mathSymbol) == "divide" or "divided":
    mathSymbol = "/"

print(val1, mathSymbol)

val2 = input("Value Two: ")

# Checks if any of the values have Pi in them.
if val1 == "pi":
    val1 = math.pi

elif val2 == "pi":
    val2 = math.pi

# Checks what symbol was inputted and calculates the answer.
if str.lower(mathSymbol) == "+":
    answer = float(val1) + float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)

elif str.lower(mathSymbol) == "-":
    answer = float(val1) - float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)

elif str.lower(mathSymbol) == "*":
    answer = float(val1) * float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)

elif str.lower(mathSymbol) == "/":
    answer = float(val1) / float(val2)
    print(float(val1), mathSymbol, float(val2), "=", answer)