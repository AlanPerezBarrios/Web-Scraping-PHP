import requests
import openpyxl

def buscar_producto_mercado_libre(producto):
    url_base = "https://api.mercadolibre.com/sites/MLM/search" #Es la url que se ocupa para poder buscar los productos, depende la region se cambia el MLM.
    params = {'q': producto} #Busqueda del usuario
    response = requests.get(url_base, params=params) #solicitud GET a Mercado Libre
    
    if response.status_code == 200:
        resultados = response.json()['results']
        productos = []
        # Iterar sobre cada resultado y extraer nombre, precio, stock y enlace (Se pueden sacar más datos)
        for resultado in resultados:
            nombre = resultado['title']
            precio = resultado['price']
            stock = resultado['available_quantity']
            link = resultado['permalink']
            productos.append([nombre, precio, stock, link])
        
        return productos
    else:
        print("Error al obtener la página")
        return None

def guardar_en_excel(datos, nombre_busqueda):
    #Nombre del archivo a guardar
    nombre_archivo = f"producto_{nombre_busqueda}.xlsx" #Se puede modificar
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active
    hoja.append(["Nombre", "Precio", "Stock", "Link"])
    # Iterar sobre cada producto en los datos y agregarlo a la hoja de Excel
    for producto in datos:
        nombre = producto[0]
        precio = f"${producto[1]}"  # Agregar el símbolo de precios al precio
        stock = producto[2]
        link = producto[3]
        hoja.append([nombre, precio, stock, link])

    libro_excel.save(nombre_archivo)

if _name_ == "_main_":
    #Instruccion para el Usuario
    producto = input("Ingrese el producto que desea buscar en Mercado Libre: ")
    # Realizar la búsqueda del producto en Mercado Libre
    info_productos = buscar_producto_mercado_libre(producto)
    
    # Verificar si se encontraron resultados para el producto
    if info_productos:
        guardar_en_excel(info_productos, producto)
        print(f"Los datos del producto '{producto}' se han guardado en un archivo correctamente.")
    else:
        print(f"No se encontraron resultados para el producto '{producto}'.")