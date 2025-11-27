# 📘 Sistema de Ventas – Cafetería Escolar

Aplicación creada en **Python**, usando **Tkinter** para la interfaz y **SQLite** como base de datos.
Permite registrar productos, realizar ventas y generar un reporte básico.

---

# 📁 Estructura del proyecto

```
Proyecto_Cafeteria/
│
├── data/
│   └── .gitkeep
│
├── docs/
│   └── README.md
│
└── src/
    ├── database.py
    ├── funciones.py
    └── plataforma.py
```

* **database.py** → crea la base de datos y tablas
* **funciones.py** → lógica del sistema (agregar, vender, eliminar, reportes)
* **plataforma.py** → interfaz gráfica con Tkinter

---

# 🚀 Cómo ejecutar

Linux / macOS:

```bash
python3 src/plataforma.py
```

Windows:

```bash
python src\plataforma.py
```

La base de datos se crea automáticamente en la carpeta `data/`.

---

# 🧩 Funcionalidades principales

* **Agregar productos** (nombre y precio)
* **Mostrar productos** en lista
* **Registrar ventas** (cantidad × precio)
* **Generar reporte de ventas**
* **Eliminar productos** con confirmación

---

# 🔒 Validaciones

* Precio ≥ 0
* Cantidad ≥ 1
* No permite nombres vacíos
* Se debe seleccionar un producto para vender o eliminar

---

# 🧱 Base de datos

Tablas:

### productos

* id
* nombre
* precio

### ventas

* id
* producto_id
* cantidad
* total

---

# 👤 Autor

Proyecto desarrollado por **L** para la práctica escolar “Cafetería Escolar”.
