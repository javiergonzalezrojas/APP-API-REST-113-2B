#Nombre: Eric Railef Mansilla
#Aplicacion API-REST

import requests

# API de productos de DummyJSON

BASE_URL= "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    #mostrar el codigo HTTP y los datos recibidos
    print("codigo HTTP", respuesta.status_code)

    if respuesta.text:
        print("respuesta JSON:")
        print(respuesta.JSON())
    else:
        print("la respuesta no tiene datos")


try:
    #=========================================
    #   1. GET: CONSULTAR UN PRODUCTO
    #=========================================

    respuesta = requests.get(
        f"{BASE_URL}/19",
        timeout=10
    )            

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("producto", producto["title"] )
    print("precio", producto["price"])
    print("categoria", producto["category"])


    #=========================================
    # 2. METODO POST
    #=========================================



except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")    