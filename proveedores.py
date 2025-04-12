import tkinter as tk
from tkinter import ttk

class ProveedoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Proveedores - Domino's Pizza")

        # Tabla
        self.tree = ttk.Treeview(root, columns=("ID", "Empresa", "Contacto", "Teléfono", "Producto"), show="headings")
        self.tree.heading("ID", text="ID Proveedor")
        self.tree.heading("Empresa", text="Nombre Empresa")
        self.tree.heading("Contacto", text="Nombre Contacto")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Producto", text="Producto Suministrado")
        self.tree.pack(pady=10, fill="x")

        # Formulario
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="ID Proveedor:").grid(row=0, column=0)
        self.id_entry = tk.Entry(frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(frame, text="Nombre Empresa:").grid(row=1, column=0)
        self.empresa_entry = tk.Entry(frame)
        self.empresa_entry.grid(row=1, column=1)

        tk.Label(frame, text="Nombre Contacto:").grid(row=2, column=0)
        self.contacto_entry = tk.Entry(frame)
        self.contacto_entry.grid(row=2, column=1)

        tk.Label(frame, text="Teléfono:").grid(row=3, column=0)
        self.telefono_entry = tk.Entry(frame)
        self.telefono_entry.grid(row=3, column=1)

        tk.Label(frame, text="Producto Suministrado:").grid(row=4, column=0)
        self.producto_entry = tk.Entry(frame)
        self.producto_entry.grid(row=4, column=1)

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
    app = ProveedoresApp(root)
    root.mainloop()
