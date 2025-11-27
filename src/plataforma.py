import tkinter as tk
import funciones

# Crear ventana

ventana = tk.Tk()
ventana.title("Sistema de Ventas - Cafetería Escolar")

# Asignarla al módulo funciones
funciones.ventana = ventana


# Boton de Agregar productos

frame_productos = tk.LabelFrame(ventana, text="Agregar Producto")
frame_productos.pack(padx=10, pady=10, fill="x")

funciones.entry_nombre = tk.Entry(frame_productos)
funciones.entry_nombre.pack(pady=5)
funciones.entry_nombre.insert(0, "Nombre del producto")

funciones.entry_precio = tk.Entry(frame_productos)
funciones.entry_precio.pack(pady=5)
funciones.entry_precio.insert(0, "0.00")

btn_agregar = tk.Button(frame_productos, text="Agregar", command=funciones.agregar_productos)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(frame_productos, text="Eliminar", command=funciones.eliminar_producto)
btn_eliminar.pack(side="left", padx=5)



# LISTA DE PRODUCTOS

funciones.lista_productos = tk.Listbox(ventana, width=50)
funciones.lista_productos.pack(padx=10, pady=5)

funciones.cargar_productos()

# Registrar venta

frame_ventas = tk.LabelFrame(ventana, text="Registrar Venta")
frame_ventas.pack(padx=10, pady=10, fill="x")

funciones.entry_cantidad = tk.Entry(frame_ventas)
funciones.entry_cantidad.pack(side="left", padx=5)
funciones.entry_cantidad.insert(0, "Cantidad")

btn_vender = tk.Button(frame_ventas, text="Registrar Venta", command=funciones.registrar_venta)
btn_vender.pack(side="left", padx=5)

# Boton de Reporte
btn_reporte = tk.Button(ventana, text="Ver Reporte de Ventas", command=funciones.mostrar_reporte)
btn_reporte.pack(pady=10)

ventana.mainloop()
