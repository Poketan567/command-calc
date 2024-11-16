
val1 = input("Value One: ")
print(int(val1))

mathSymbol = input("Symbol: ")
print(int(val1), mathSymbol)

val2 = input("Value Two: ")

if mathSymbol == "+":
    answer = int(val1) + int(val2)
    print(int(val1), mathSymbol, int(val2), "=", answer)

elif mathSymbol == "-":
    answer = int(val1) - int(val2)
    print(int(val1), mathSymbol, int(val2), "=", answer)

elif mathSymbol == "*":
    answer = int(val1) * int(val2)
    print(int(val1), mathSymbol, int(val2), "=", answer)

elif mathSymbol == "/":
    answer = int(val1) / int(val2)
    print(int(val1), mathSymbol, int(val2), "=", answer)