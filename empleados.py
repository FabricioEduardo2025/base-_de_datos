from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def mostrar_empleados():
    
    def conectar_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Edu@rdo15",
            database="dominos"
        )

    def insertar_empleado(nombre, apellido, telefono, email, direccion, refrescar):
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO empleados (nombre, apellido, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s)",
                           (nombre.get(), apellido.get(), telefono.get(), email.get(), direccion.get()))
            conn.commit()
            conn.close()
            refrescar()
            limpiar_empleado(nombre, apellido, telefono, email, direccion)
            messagebox.showinfo("Éxito", "Empleado insertado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_empleado(tree, refrescar):
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Selecciona un empleado para eliminar.")
            return
        id_empleado = tree.item(item)["values"][0]
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM empleados WHERE id_empleados=%s", (id_empleado,))
            conn.commit()
            conn.close()
            refrescar()
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_empleado(tree, nombre, apellido, telefono, email, direccion, refrescar):
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Selecciona un empleado para actualizar.")
            return
        try:
            id_empleado = tree.item(item)["values"][0]
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("""UPDATE empleados 
                              SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s 
                              WHERE id_empleados=%s""",
                           (nombre.get(), apellido.get(), telefono.get(), email.get(), direccion.get(), id_empleado))
            conn.commit()
            conn.close()
            refrescar()
            limpiar_empleado(nombre, apellido, telefono, email, direccion)
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_empleado(nombre, apellido, telefono, email, direccion):
        for campo in [nombre, apellido, telefono, email, direccion]:
            campo.delete(0, END)

    # VENTANA PRINCIPAL
    nuevo = Tk()
    nuevo.title("Gestión de Empleados")
    nuevo.geometry("950x600")
    nuevo.minsize(800, 500)

    nuevo.columnconfigure(0, weight=3)
    nuevo.columnconfigure(1, weight=1)
    nuevo.rowconfigure(0, weight=1)

    izquierda_emp = Frame(nuevo)
    izquierda_emp.grid(row=0, column=0, sticky="nsew")

    tree_emp = ttk.Treeview(izquierda_emp, columns=("ID", "Nombre", "Apellido", "Teléfono", "Email", "Dirección"), show="headings", height=20)
    for col in tree_emp["columns"]:
        tree_emp.heading(col, text=col)
        tree_emp.column(col, width=120, anchor="center")
    tree_emp.pack(fill="both", expand=True, padx=10, pady=10)

    def cargar_empleados():
        for row in tree_emp.get_children():
            tree_emp.delete(row)
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id_empleados, nombre, apellido, telefono, email, direccion FROM empleados")
        for row in cursor.fetchall():
            tree_emp.insert("", "end", values=row)
        conn.close()

    cargar_empleados()

    derecha_emp = Frame(nuevo, bg="#ffeaa7")
    derecha_emp.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    formulario_emp = Frame(derecha_emp, bg="#ffeaa7")
    formulario_emp.pack(pady=10, fill="x")  # Se muestra siempre sin opción a ocultar

    etiquetas = ["Nombre", "Apellido", "Teléfono", "Email", "Dirección"]
    entradas = {}
    for etiqueta in etiquetas:
        Label(formulario_emp, text=etiqueta + ":", bg="#ffeaa7").pack()
        entrada = Entry(formulario_emp)
        entrada.pack(fill="x")
        entradas[etiqueta.lower()] = entrada

    Button(derecha_emp, text="Insertar", command=lambda: insertar_empleado(
        entradas["nombre"], entradas["apellido"], entradas["teléfono"], entradas["email"], entradas["dirección"], cargar_empleados), bg="#81ecec").pack(pady=5, fill="x")
    Button(derecha_emp, text="Actualizar", command=lambda: actualizar_empleado(
        tree_emp, entradas["nombre"], entradas["apellido"], entradas["teléfono"], entradas["email"], entradas["dirección"], cargar_empleados), bg="#74b9ff").pack(pady=5, fill="x")
    Button(derecha_emp, text="Eliminar", command=lambda: eliminar_empleado(tree_emp, cargar_empleados), bg="#ff7675").pack(pady=5, fill="x")

    def cargar_empleado_form(event):
        selected = tree_emp.selection()
        if selected:
            datos = tree_emp.item(selected)["values"]
            for i, key in enumerate(etiquetas):
                entradas[key.lower()].delete(0, END)
                entradas[key.lower()].insert(0, datos[i+1])
            formulario_emp.pack(pady=10, fill="x")

    tree_emp.bind("<<TreeviewSelect>>", cargar_empleado_form)

    nuevo.mainloop()

if __name__== "__main__":
    mostrar_empleados()
