
TIPO_DE_PAQUETE =['pequeño','mediano','grande']
SECTOR = ['centro','norte','sur']
cantPequeños = 0
cantMedianos = 0
cantGrande = 0
cantPaquetes = []
#1 registrar pedidos, no entiendo pq no me deja agregar el.append 
def Registrar_pedido(pedidos):
    print("Solicitando datos del cliente...")
    nombre = input("ingrese nombre y apellido del cliente: ")
    direccion = input("ingrese direccion del cliente: ")
    sector = input("ingrese sector del cliente porfavor: ")
    detallePedido = input("escriba su tipo de paquete,(Pequeño, Mediano, Grande):").lower()
    while detallePedido not in TIPO_DE_PAQUETE:
        print("opcion no valida, ingrese nuevamente")
        detallePedido = input("escriba su tipo de paquete,(Pequeño, Mediano, Grande):").lower()
    if detallePedido == "pequeño":
        paquetes = int(input("ingrese cantiddad de paquetes pequeños:"))
        cantPequeños = cantPequeños +paquetes
    elif detallePedido == "mediano":
        paquetes = int(input("ingrese la cantidad de paquetes medianos :"))
        cantMedianos = cantMedianos + paquetes
    elif detallePedido == "grande":
        paquetes = int(input("ingrese la cantidad de paquetes grandes: "))
        cantGrande = cantGrande + paquetes
    datos ={
         'Nombre': nombre,
         'Direccion': direccion,
         'Sector': sector,
         'Paquetes': detallePedido
    }
    pedidos.append(datos)
#2 listar pedidos
def Listar_Pedidos(pedidos):
    for i in pedidos:
        print(pedidos)
#3 imprimir hoja de ruta
def Imprimir_hoja(pedidos):
        Sector = input("ingrese sector (centro,norte,sur): ").lower
        while Sector not in SECTOR:
             print("error de sector intente nuevamente")
             Sector = input("ingrese sector (centro,norte,sur): ").lower
        with open('detallepedido.txt','w',newline="") as archivo:
             archivo.write()
        print()
