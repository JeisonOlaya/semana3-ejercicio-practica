# Datos iniciales
boletos = {}
contador = 1
rutas = {
    "1": {"nombre": "Bogotá - Medellín", "tipo": "nacional", "precio": 230000},
    "2": {"nombre": "Bogotá - España", "tipo": "internacional", "precio": 4200000},
    "3": {"nombre": "Bogota - Alemania","tipo": "internacional", "precio": 5350000},
    "4": {"nombre": "Bogota - Cartagena","tipo": "nacional", "precio": 50000}
}

def main():
    while True:
        print("\nSISTEMA DE BOLETOS DE AVIÓN")
        print("1. Comprar boleto")
        print("2. Ver boleto")
        print("3. Modo administrador")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            comprar_boleto()
        elif opcion == "2":
            ver_boleto()
        elif opcion == "3":
            administrador()
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida")

def comprar_boleto():
    global contador, boletos
    
    print("\nCOMPRAR BOLETO")
    print("Rutas disponibles:")
    for num, ruta in rutas.items():
        print(rutas)
    
    ruta = input("Elige el número de ruta: ")
    if ruta not in rutas:
        print("Ruta no válida")
        return
    
    nombre = input("Nombre del pasajero: ")
    fecha = input("Fecha del vuelo (DD/MM/AAAA): ")
    
    # Equipaje principal
    peso = float(input("Peso equipaje principal (kg): "))
    if peso > 50:
        estado_equipaje = "Excedido (no permitido)"
        costo_extra = 0
    elif peso > 30:
        estado_equipaje = "Peso aceptado (70,000 extra)"
        costo_extra = 70000
    elif peso > 20:
        estado_equipaje = "Peso aceptado (50,000 extra)"
        costo_extra = 50000
    else:
        estado_equipaje = "Peso normal (sin costo extra)"
        costo_extra = 0
    
    # Equipaje de mano
    tiene_mano = input("¿Lleva equipaje de mano? (si/no): ").lower()
    if tiene_mano == "si":
        peso_mano = float(input("Peso equipaje de mano (kg): "))
        if peso_mano > 13:
            estado_mano = "Excedido (no permitido)"
        else:
            estado_mano = "Aceptado"
    else:
        estado_mano = "Sin equipaje de mano"
    
    # Calcular total
    total = rutas[ruta]["precio"] + costo_extra
    
    # Guardar boleto
    id_boleto = f"BOLETO-{contador}"
    boletos[id_boleto] = {
        "nombre": nombre,
        "ruta": rutas[ruta]["nombre"],
        "fecha": fecha,
        "equipaje": estado_equipaje,
        "equipaje_mano": estado_mano,
        "total": total
    }
    contador += 1
    
    print("\n¡Boleto comprado con éxito!")
    print(f"Tu número de boleto es: {id_boleto}")

def ver_boleto():
    print("\nVER BOLETO")
    id_boleto = input("Ingresa tu número de boleto: ")
    
    if id_boleto not in boletos:
        print("Boleto no encontrado")
        return
    
    boleto = boletos[id_boleto]
    print("\n--- INFORMACIÓN DEL BOLETO ---")
    print(f"Pasajero: {boleto['nombre']}")
    print(f"Ruta: {boleto['ruta']}")
    print(f"Fecha: {boleto['fecha']}")
    print(f"Equipaje principal: {boleto['equipaje']}")
    print(f"Equipaje de mano: {boleto['equipaje_mano']}")
    print(f"TOTAL PAGADO: ${boleto['total']:,}")

def administrador():
    clave = input("\nIngresa la clave de administrador: ")
    if clave != "admin123":
        print("Clave incorrecta")
        return
    
    while True:
        print("\nMODO ADMINISTRADOR")
        print("1. Ver todas las ventas")
        print("2. Ver ganancias totales")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print("\n--- TODOS LOS BOLETOS ---")
            for id_boleto, boleto in boletos.items():
                print(f"\nBoleto: {id_boleto}")
                print(f"Pasajero: {boleto['nombre']}")
                print(f"Total: ${boleto['total']:,}")
        elif opcion == "2":
            total = sum(boleto['total'] for boleto in boletos.values())
            print(f"\nGANANCIAS TOTALES: ${total:,}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

# Iniciar el programa
if __name__ == "__main__":
    main()