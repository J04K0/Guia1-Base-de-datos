from pymongo import MongoClient

#Conexión a la base de datos
client = MongoClient("mongodb://localhost:27017/")
baseDatos = client["Tienda"]
coleccion = baseDatos["Despensa"]


#Mostrar productos
def consultarProductos():
    for post in coleccion.find():
        print("Producto:",post["producto"], "Categoria:",post["categoria"], "Precio:",post["precio"])

#Insertar productos
def insertarProducto():
    producto = input("Introduzca el producto: ")
    categoria = input("Introduzca la categoria: ")
    precio = input("Introduzca el precio: ")
    nuevoProducto = {"producto": producto, "categoria": categoria, "precio": precio}
    coleccion.insert_one(nuevoProducto)
    print("Producto insertado correctamente")


#Actualizar productos
def actualizarProducto():
    producto = input("Introduzca el producto a actualizar: ")
    nuevoProducto = input("Introduzca el nuevo producto: ")
    nuevaCategoria = input("Introduzca la nueva categoria: ")
    nuevoPrecio = input("Introduzca el nuevo precio: ")
    coleccion.update_one({"producto": producto}, {"$set": {"producto": nuevoProducto, "categoria": nuevaCategoria, "precio": nuevoPrecio}})
    print("Producto actualizado correctamente")
    

#Eliminar productos
def eliminarProducto():
    producto = input("Introduzca el producto a eliminar: ")
    coleccion.delete_one({"producto": producto})
    print("Producto eliminado correctamente")

def mostrarMenu():
    print("1. Consultar productos")
    print("2. Insertar productos")
    print("3. Actualizar productos")
    print("4. Eliminar productos")
    print("5. Salir")

def main():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultarProductos()
        elif opcion == "2":
            insertarProducto()
        elif opcion == "3":
            actualizarProducto()
        elif opcion == "4":
            eliminarProducto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

