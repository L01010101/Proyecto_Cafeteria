import tkinter as tk
from tkinter import messagebox
from database import conn, cursor

# Estas variables son asignadas por plataforma.py
entry_nombre = None
entry_precio = None
entry_cantidad = None
lista_productos = None
ventana = None


# Cargar productos en la lista
def cargar_productos():
    lista_productos.delete(0, tk.END)
    cursor.execute("SELECT id, nombre, precio FROM productos")
    for row in cursor.fetchall():
        lista_productos.insert(tk.END, f"{row[0]} - {row[1]} - ${row[2]:.2f}")

# Agregar un producto
def agregar_productos():
    nombre = entry_nombre.get()
    precio = entry_precio.get()

    if not nombre or not precio:
        messagebox.showwarning("Error", "Complete todos los campos")
        return

    try:
        precio = float(precio)
        if precio <= 0:
            raise ValueError
    except:
        messagebox.showwarning("Error", "El precio debe ser un numero mayor a 0")
        return

    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()

    messagebox.showinfo("Éxito", "Producto agregado correctamente")

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    cargar_productos()

# Registrar una venta
def registrar_venta():
    seleccion = lista_productos.curselection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Seleccione un producto")
        return

    producto_texto = lista_productos.get(seleccion)
    producto_id = int(producto_texto.split(" - ")[0])

    try:
        cantidad = int(entry_cantidad.get())
        if cantidad <= 0:
            raise ValueError
    except:
        messagebox.showwarning("Error", "Cantidad inválida")
        return

    cursor.execute("SELECT precio FROM productos WHERE id = ?", (producto_id,))
    precio = cursor.fetchone()[0]
    total = precio * cantidad

    cursor.execute("INSERT INTO ventas (producto_id, cantidad, total) VALUES (?, ?, ?)", (producto_id, cantidad, total))
    conn.commit()

    messagebox.showinfo("Venta registrada", f"Total: ${total:.2f}")
    entry_cantidad.delete(0, tk.END)

# Eliminar Producto
def eliminar_producto():
    seleccion = lista_productos.curselection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Seleccione un producto para eliminar.")
        return

    producto_texto = lista_productos.get(seleccion[0])
    producto_id = int(producto_texto.split(" - ")[0])

    # Confirmación
    confirm = messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar el producto ID {producto_id}?")
    if not confirm:
        return

    # Eliminar ventas relacionadas primero 
    cursor.execute("DELETE FROM ventas WHERE producto_id = ?", (producto_id,))

    # Eliminar producto
    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conn.commit()

    messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")
    cargar_productos()


# Mostrar reporte de ventas
def mostrar_reporte():
    reporte = tk.Toplevel(ventana)
    reporte.title("Reporte de Ventas")

    texto = tk.Text(reporte, width=60, height=20)
    texto.pack(padx=10, pady=10)

    cursor.execute("""
        SELECT productos.nombre, SUM(ventas.cantidad), SUM(ventas.total)
        FROM ventas
        JOIN productos ON productos.id = ventas.producto_id
        GROUP BY productos.nombre
        ORDER BY SUM(ventas.cantidad) DESC
    """)

    resultados = cursor.fetchall()

    texto.insert(tk.END, "REPORTE DE VENTAS\n\n")
    for nombre, cantidad, total in resultados:
        texto.insert(tk.END, f"Producto: {nombre}\nCantidad vendida: {cantidad}\nTotal generado: ${total:.2f}\n\n")

    texto.config(state="disabled")
