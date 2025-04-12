import tkinter as tk
from tkinter import ttk

class ProductosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos - Domino's Pizza")

        # Tabla
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Tipo", "Tamaño", "Precio", "Descripción"), show="headings")
        self.tree.heading("ID", text="ID Producto")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Tamaño", text="Tamaño")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10, fill="x")

        # Formulario
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="ID Producto:").grid(row=0, column=0)
        self.id_entry = tk.Entry(frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(frame, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(frame, text="Tipo (Pizza/Pollo):").grid(row=2, column=0)
        self.tipo_entry = tk.Entry(frame)
        self.tipo_entry.grid(row=2, column=1)

        tk.Label(frame, text="Tamaño:").grid(row=3, column=0)
        self.tamano_entry = tk.Entry(frame)
        self.tamano_entry.grid(row=3, column=1)

        tk.Label(frame, text="Precio:").grid(row=4, column=0)
        self.precio_entry = tk.Entry(frame)
        self.precio_entry.grid(row=4, column=1)

        tk.Label(frame, text="Descripción:").grid(row=5, column=0)
        self.descripcion_entry = tk.Entry(frame)
        self.descripcion_entry.grid(row=5, column=1)

        # Botones DML
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Insertar", width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Actualizar", width=10).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", width=10).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Consultar", width=10).grid(row=0, column=3, padx=5)

# Ejecutar interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = ProductosApp(root)
    root.mainloop()
