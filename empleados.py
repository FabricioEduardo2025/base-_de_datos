import tkinter as tk
from tkinter import ttk

class EmpleadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados - Domino's Pizza")

        # Tabla
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Puesto", "Teléfono", "Turno"), show="headings")
        self.tree.heading("ID", text="ID Empleado")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Puesto", text="Puesto")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Turno", text="Turno")
        self.tree.pack(pady=10, fill="x")

        # Formulario
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="ID Empleado:").grid(row=0, column=0)
        self.id_entry = tk.Entry(frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(frame, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(frame, text="Puesto:").grid(row=2, column=0)
        self.puesto_entry = tk.Entry(frame)
        self.puesto_entry.grid(row=2, column=1)

        tk.Label(frame, text="Teléfono:").grid(row=3, column=0)
        self.telefono_entry = tk.Entry(frame)
        self.telefono_entry.grid(row=3, column=1)

        tk.Label(frame, text="Turno:").grid(row=4, column=0)
        self.turno_entry = tk.Entry(frame)
        self.turno_entry.grid(row=4, column=1)

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
    app = EmpleadosApp(root)
    root.mainloop()
