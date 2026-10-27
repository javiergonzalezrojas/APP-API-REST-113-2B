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
    
    print("\n GET --- crear un producto---")
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

    print("\n POST --- crear un producto---")

    nuevo_producto = {
        "title": "teclado mecanico gamer",
        "price": "90000",
        "description": "teclado para juegos",
        "category": "electronics"
    }

    respuesta = requests.post(
        f"{BASE_URL}/add",
        json=nuevo_producto,
        timeout=10
    )

    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)

    #==========================================
    #3.   METODO PUT
    #==========================================

    print("\n --- PUT: actualizar un producto ---")

    producto_actualizado = {
        "title": "notebook para desarrollar",
        "price": "590000",
        "description": "noteboo para programar",
        "category": "laptops",
    }

    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)


except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")    