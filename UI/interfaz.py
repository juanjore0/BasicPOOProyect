from Modelos.modelo import Cuenta

def crear_cuenta():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    documento_id = int(input("Ingrese el documento de identidad: "))
    nombre = input("Ingrese el nombre del cliente: ")
    saldo = float(input("Ingrese el saldo inicial: "))

    return Cuenta(numero_cuenta, documento_id, nombre, saldo)

def mostrar_info(cuenta):
    print("\n📌 Información de la Cuenta 📌")
    print(f"Número de Cuenta: {cuenta._Cuenta__numero_cuenta}") 
    print(f"Documento de Identidad: {cuenta.documento_id}")
    print(f"Nombre del Cliente: {cuenta.nombre}")
    print(f"Saldo Actual: ${cuenta.saldo:.2f}\n")

def menu():
    """Muestra el menú de opciones al usuario"""
    print("\n🌟 Menú de Opciones 🌟")
    print("1. Crear Cuenta")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Mostrar Información de la Cuenta")
    print("5. Salir")

def main_interfaz():
    cuentaClientes = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cuenta = crear_cuenta()
            cuentaClientes.append(cuenta)
            print("✅ Cuenta creada exitosamente.")

        elif opcion == "2":
            if cuentaClientes:
                num_cuenta = int(input("Ingrese el número de cuenta: "))
                cuenta = next((c for c in cuentaClientes if c._Cuenta__numero_cuenta == num_cuenta), None)
                if cuenta:
                    cantidad = float(input("Ingrese la cantidad a depositar: "))
                    cuenta.depositar_dinero(cantidad)
                else:
                    print("❌ Cuenta no encontrada.")
            else:
                print("❌ No hay cuentas registradas.")

        elif opcion == "3":
            if cuentaClientes:
                num_cuenta = int(input("Ingrese el número de cuenta: "))
                cuenta = next((c for c in cuentaClientes if c._Cuenta__numero_cuenta == num_cuenta), None)
                if cuenta:
                    cantidad = float(input("Ingrese la cantidad a retirar: "))
                    cuenta.retirar_dinero(cantidad)
                else:
                    print("❌ Cuenta no encontrada.")
            else:
                print("❌ No hay cuentas registradas.")

        elif opcion == "4":
            if cuentaClientes:
                num_cuenta = int(input("Ingrese el número de cuenta: "))
                cuenta = next((c for c in cuentaClientes if c._Cuenta__numero_cuenta == num_cuenta), None)
                if cuenta:
                    mostrar_info(cuenta) 
                else:
                    print("❌ Cuenta no encontrada.")
            else:
                print("❌ No hay cuentas registradas.")

        elif opcion == "5":
            print("👋 Saliendo del sistema. ¡Gracias por usar nuestro banco!")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")