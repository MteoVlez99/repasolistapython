# listas [corchetes] (arreglos) y diccionario {llaves}(objetos)
clienteUno = {
    "id":5,
    "nombre":"edificio1",
    "consumo":200
}

clienteDos = {
    "id":58,
    "nombre":"edificio2",
    "consumo":500
}

#Liastas de diccionario
clientes =[ 
    clienteUno,
    clienteDos
]

'''for i in (1,21,5): # el 1 es donde inicia, el 21 es donde finaliza menos 1, e5 5 es las veces que incrementa la variable iterradora
    print(i)'''

'''for i in range(2):
    print(clientes[i]["consumo"])'''

for cliente in clientes:
    print(cliente["id"],"->",cliente["consumo"],"kwh")
    print(f"{cliente['id']} => {cliente['consumo']} kwh")
 