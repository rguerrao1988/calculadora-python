def calculadora(num_1, operacion, num_2):
    
    
    if operacion == "+":
        return num_1 + num_2
    elif operacion == '-':
        return num_1 - num_2
    elif operacion == '*' or operacion == "x": # ususario puede usar  * ó x
        return num_1 * num_2
    elif operacion == '/':
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"
total = calculadora(int(input("primer numero: ")), str(input("operador? ")), int(input("segundo numero: ")),)
print(total)          
