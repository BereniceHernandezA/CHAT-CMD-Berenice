import xmlrpc.client

# Conexión al Servidor 🌸🩰
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Menú de opciones y funciones remotas 🌸🩰
opciones = {
    1: ("Sumar", server.sumar),
    2: ("Restar", server.restar),
    3: ("Multiplicar", server.multiplicar),
    4: ("Dividir", server.dividir)
}

def menu():
    # Mostrar el menú de opciones al usuario 🌸🩰
    print("\nCalculadora Remota")
    for key, (nombre, _) in opciones.items():
        print(f"{key}. {nombre}")
    print("5. Salir")
    return int(input("Selecciona una opción: "))

while True:
    # Solicitar al usuario que seleccione una opción 🌸🩰
    opcion = menu()
    if opcion == 5:
        # Finalizar la ejecución 🌸🩰
        print("\u00a1Adiós! Mi tarea ha sido completada")
        break

    if opcion in opciones:
        # Solicitar los números para la operación seleccionada 🌸🩰
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        nombre, funcion = opciones[opcion]
        # Mostrar el resultado de la operación 🌸🩰
        print(f"Resultado: {funcion(num1, num2)}")
    else:
        # Indicar que la opción ingresada no es válida 🌸🩰
        print("Opción no válida. Intenta de nuevo.")
