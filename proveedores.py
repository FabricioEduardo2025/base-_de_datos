from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def mostrar_proveedores():
    
    def conectar_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Edu@rdo15",
            database="dominos"
        )

    def insertar_proveedor(nombre, contacto, telefono, email, direccion, tipo, refrescar):
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO proveedores 
                              (nombre, contacto, telefono, email, direccion, tipo) 
                              VALUES (%s, %s, %s, %s, %s, %s)""",
                           (nombre.get(), contacto.get(), telefono.get(), email.get(), direccion.get(), tipo.get()))
            conn.commit()
            conn.close()
            refrescar()
            limpiar_proveedor(nombre, contacto, telefono, email, direccion, tipo)
            messagebox.showinfo("Éxito", "Proveedor insertado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_proveedor(tree, refrescar):
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Selecciona un proveedor para eliminar.")
            return
        id_proveedor = tree.item(item)["values"][0]
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id_provedor=%s", (id_proveedor,))
            conn.commit()
            conn.close()
            refrescar()
            messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_proveedor(tree, nombre, contacto, telefono, email, direccion, tipo, refrescar):
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Selecciona un proveedor para actualizar.")
            return
        id_proveedor = tree.item(item)["values"][0]
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("""UPDATE proveedores 
                              SET nombre=%s, contacto=%s, telefono=%s, email=%s, direccion=%s, tipo=%s 
                              WHERE id_provedor=%s""",
                           (nombre.get(), contacto.get(), telefono.get(), email.get(), direccion.get(), tipo.get(), id_proveedor))
            conn.commit()
            conn.close()
            refrescar()
            limpiar_proveedor(nombre, contacto, telefono, email, direccion, tipo)
            messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_proveedor(nombre, contacto, telefono, email, direccion, tipo):
        for campo in [nombre, contacto, telefono, email, direccion]:
            campo.delete(0, END)
        tipo.set('')

    # --- INTERFAZ PRINCIPAL ---
    ventana = Tk()
    ventana.title("Gestión de Proveedores - Domino's Pizza")
    ventana.geometry("950x600")
    ventana.minsize(800, 500)

    ventana.columnconfigure(0, weight=3)
    ventana.columnconfigure(1, weight=1)
    ventana.rowconfigure(0, weight=1)

    # --- IZQUIERDA: Tabla ---
    frame_izquierda = Frame(ventana)
    frame_izquierda.grid(row=0, column=0, sticky="nsew")

    tree_prov = ttk.Treeview(frame_izquierda, columns=("ID", "Nombre", "Contacto", "Teléfono", "Email", "Dirección", "Tipo"), show="headings", height=20)
    for col in tree_prov["columns"]:
        tree_prov.heading(col, text=col)
        tree_prov.column(col, width=120, anchor="center")
    tree_prov.pack(fill="both", expand=True, padx=10, pady=10)

    def cargar_proveedores():
        for row in tree_prov.get_children():
            tree_prov.delete(row)
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id_provedor, nombre, contacto, telefono, email, direccion, tipo FROM proveedores")
        for row in cursor.fetchall():
            tree_prov.insert("", "end", values=row)
        conn.close()

    cargar_proveedores()

    # --- DERECHA: Formulario y Botones ---
    frame_derecha = Frame(ventana, bg="#fab1a0")
    frame_derecha.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    formulario = Frame(frame_derecha, bg="#fab1a0")
    formulario.pack(fill="x", pady=(0, 10))  # Mostrado desde el inicio

    etiquetas = ["Nombre", "Contacto", "Teléfono", "Email", "Dirección"]
    entradas = {}
    for etiqueta in etiquetas:
        Label(formulario, text=etiqueta + ":", bg="#fab1a0").pack()
        entrada = Entry(formulario)
        entrada.pack(fill="x")
        entradas[etiqueta.lower()] = entrada

    Label(formulario, text="Tipo:", bg="#fab1a0").pack()
    tipo_var = StringVar()
    tipo_combo = ttk.Combobox(formulario, textvariable=tipo_var, state="readonly")
    tipo_combo["values"] = ("ingredientes", "bebidas", "empaques", "otros")
    tipo_combo.pack(fill="x")

    # Botones debajo del formulario
    Button(frame_derecha, text="Insertar", command=lambda: insertar_proveedor(
        entradas["nombre"], entradas["contacto"], entradas["teléfono"],
        entradas["email"], entradas["dirección"], tipo_var, cargar_proveedores), bg="#81ecec").pack(pady=5, fill="x")

    Button(frame_derecha, text="Actualizar", command=lambda: actualizar_proveedor(
        tree_prov, entradas["nombre"], entradas["contacto"], entradas["teléfono"],
        entradas["email"], entradas["dirección"], tipo_var, cargar_proveedores), bg="#74b9ff").pack(pady=5, fill="x")

    Button(frame_derecha, text="Eliminar", command=lambda: eliminar_proveedor(
        tree_prov, cargar_proveedores), bg="#ff7675").pack(pady=5, fill="x")

    def cargar_form_proveedor(event):
        selected = tree_prov.selection()
        if selected:
            datos = tree_prov.item(selected)["values"]
            for i, key in enumerate(etiquetas):
                entradas[key.lower()].delete(0, END)
                entradas[key.lower()].insert(0, datos[i+1])
            tipo_var.set(datos[6])

    tree_prov.bind("<<TreeviewSelect>>", cargar_form_proveedor)

    ventana.mainloop()

if __name__ == "__main__":
    mostrar_proveedores()

#20 de mayo