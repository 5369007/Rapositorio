import math

print("""+ soma, * multiplicação,  ** potencia
- subtração, / divisão, // raiz quadrada
ps: Para números decimais utilizar \".\"
ou invés de \",\".
""")

x = float(input("1º número: "))
o = input("Operação desejada: ")
if o != "//":
    y = float(input("2° número: "))
stop = ""

if o == "+":
    r = x + y
elif o == "-":
    r = x - y
elif o == "*":
    r = x * y
elif o == "/":
    r = x / y
elif o == "**":
    r = x ** y
elif o == "//":
    r = math.sqrt(x)
else:
    print("Operador invalido")

print(r)
stop = input("Deseja parar ou restartar? y/r press any to continue: ")

while stop != "y":
    if stop == "r":
        r = float(input("1º número: "))
        stop = ""
    o = input("Operação desejada: ")
    if o != "//":
        y = float(input("2° número: "))

    if o == "+":
        r = r + y
    elif o == "-":
        r = r - y
    elif o == "*":
        r = r * y
    elif o == "/":
        r = r / y
    elif o == "**":
        r = r ** y
    elif o == "//":
        r = math.sqrt(r)
    else:
        print("Operador invalido")
    print(r)
    stop = input("Deseja parar ou restartar? y/r press any to continue: ")
print("Resultado final :",r)
input("Até mais!")
