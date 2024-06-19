import funciones as fn
pedidos=[]



while True:
    print("     EMPRESA DE REPARTO PaquExpress   ")
    print("1. Registrar pedido")
    print("2. Listar los todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")
    opcion = int(input("ingrese su opcion: "))
    if opcion == 1:
        fn.Registrar_pedido
    elif opcion ==2:
        fn.Imprimir_hoja
    elif opcion == 3:
        fn.Imprimir_hoja
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("error ingrese una opcion valida")
