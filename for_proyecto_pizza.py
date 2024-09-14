#proyecto de pizzería Programación Fácil
'''
título Pizzería ABC
El usuario introduce dinero y se guarda como variable
Crear lista para ingredientes extra. Pista: métodos como adición en listas.
Habrá mínimo3 tipos de pizzas a elegir.
Cada pizza tiene precio diferente.
El usuario puede elegir sólo una pizza.
Una vez elegida se muestra el valor del total.
Añade al menos 3 ingredientes. Si se pasa del dinero se le dirá que no llega.
Las pizzas e ingre4dientes tendrán sus precios almacenados en variables.
Con cada ingrediente extra, se debe ir sumando al precio total y mostrar al usuario con el cambio.
'''

#precios pizza
pepperoni = 13.95
hawaiana = 15.59
carnivora = 17.30

#precios ingredientes / extra

dinero = float(input("Ingresa el monto del dinero que tienes para la compra de tu producto: "))
total= 0
pedido = []

anchoa = 2.2
queso = 1.9
piña = 2.3

print("Pizzería ABC")

print(f"Ha ingresado {dinero} soles para su compra.")

while True: 
    #Menú de pizzas
    print(f'1 - Pizza de Pepperoni - {pepperoni} soles\n2 - Pizza Hawaiana - {hawaiana} soles\n3 - Pizza Carnívora - {carnivora} soles')
    
    pizza_elegida = int(input("Seleccionse 1,2 o 3 para elegir su pizza elegida: "))

    match pizza_elegida:   
        case 1:
            print(f"Ha elegido la pizza Pepperoni.\nEl total a pagar es {pepperoni} soles. ")
            dinero -= pepperoni
            print(f"Le quedan {round(dinero,2)} soles.")
            total += pepperoni
            pedido.append(f"pepperoni - {pepperoni} soles")
            break
        case 2:
            print(f"Ha elegido la pizza Hawaiana.\nEl total a pagar es {hawaiana} soles. ")
            dinero -= hawaiana
            print(f"Le quedan {round(dinero,2)} soles.")
            total +=hawaiana
            pedido.append(f"hawaiana - {hawaiana} soles")
            break
        case 3:
            print(f"Ha elegido la pizza Hawaiana.\nEl total a pagar es {carnivora} soles. ")
            dinero -= carnivora
            print(f"Le quedan {round(dinero,2)} soles.")
            total +=carnivora
            pedido.append(f"hawaiana - {carnivora} soles")
            break
        case _:
            print(f"Has elegido una opción no válida. Seleccione dentro de las opciones del 1 al 3.")

print("\n---Pasamos a la elección de ingredientes---\n")

while True:
    print(f"1 - Anchoa - {anchoa} soles\n2 - Queso - {queso} soles\n3 - Piña - {piña} soles"
          "\n4 - No añadir extra y pagar")

    ingred_extra = int(input("Si desea algún ingrediente extra, porfavor elija entre estas opciones: "))

    match ingred_extra:
        case 1:
            print(f"Ha elegido el extra de anchoa.\nExtra a pagar es {anchoa} soles.")
            dinero -= anchoa
            total += anchoa
            print(f"Total a pagar: {total} soles.")
            print(f"Le quedan {round(dinero,2)} soles.")
            pedido.append(f"Extra de anchoa - {anchoa} soles")
        case 2:
            print(f"Ha elegido el extra de anchoa.\nExtra a pagar es {queso} soles.")
            dinero -= queso
            total += queso
            print(f"Total a pagar: {total} soles.")
            print(f"Le quedan {round(dinero,2)} soles.")
            pedido.append(f"Extra de queso - {queso} soles")
        case 3:
            print(f"Ha elegido el extra de piña.\nExtra a pagar es {piña} soles.")
            dinero -= piña
            total += piña
            print(f"Total a pagar: {total} soles.")
            print(f"Le quedan {round(dinero,2)} soles.")
            pedido.append(f"Extra de piña - {piña} soles")
        case 4:
            print("De acuerdo. No se añade un uxtra a tu pedido")  
            break
        case _:
            print(f"Opción incorrecta. Seleccione dentro de las opciones del 1 al 3.")

if total <= dinero:
    print("\n---Su Pedido---\n")

    print(f"El total del pedido es: {total} soles.")
    print(f"Su cambio es: {dinero} soles.\n")

    for i in pedido:
        print(f"Su pedido consta de - {i}.")

    print("\nBuen provecho")

else: 
    print("El monto ingesado al inicio es menor de lo que puede comprar. POrfavor inicie de nuevo la transacción")



