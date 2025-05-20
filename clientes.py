from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def mostrar_clientes():
 def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Edu@rdo15",
        database="dominos"
    )

 def insertar_cliente(nombre, apellido, telefono, email, direccion, refrescar):
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clientes (nombre, apellido, telefono, email, direccion)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre.get(), apellido.get(), telefono.get(), email.get(), direccion.get()))
        conn.commit()
        conn.close()
        refrescar()
        limpiar_cliente(nombre, apellido, telefono, email, direccion)
        messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 def eliminar_cliente(tree, refrescar):
    item = tree.selection()
    if not item:
        messagebox.showwarning("Advertencia", "Selecciona un cliente para eliminar.")
        return
    id_cliente = tree.item(item)["values"][0]
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id_cliente,))
        conn.commit()
        conn.close()
        refrescar()
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 def actualizar_cliente(tree, nombre, apellido, telefono, email, direccion, refrescar):
    item = tree.selection()
    if not item:
        messagebox.showwarning("Advertencia", "Selecciona un cliente para actualizar.")
        return
    id_cliente = tree.item(item)["values"][0]
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE clientes SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s
            WHERE id_cliente=%s
        """, (nombre.get(), apellido.get(), telefono.get(), email.get(), direccion.get(), id_cliente))
        conn.commit()
        conn.close()
        refrescar()
        limpiar_cliente(nombre, apellido, telefono, email, direccion)
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 def limpiar_cliente(nombre, apellido, telefono, email, direccion):
    for campo in [nombre, apellido, telefono, email, direccion]:
        campo.delete(0, END)

 # --- Interfaz ---
 ventana = Tk()
 ventana.title("Gestión de Clientes")
 ventana.geometry("900x500")

 frame_izquierda = Frame(ventana)
 frame_izquierda.pack(side=LEFT, fill=BOTH, expand=True)

 tree_clientes = ttk.Treeview(frame_izquierda, columns=("ID", "Nombre", "Apellido", "Teléfono", "Email", "Dirección"), show="headings")
 for col in tree_clientes["columns"]:
    tree_clientes.heading(col, text=col)
    tree_clientes.column(col, width=100)
 tree_clientes.pack(fill=BOTH, expand=True, padx=10, pady=10)

 def cargar_clientes():
    for row in tree_clientes.get_children():
        tree_clientes.delete(row)
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id_cliente, nombre, apellido, telefono, email, direccion FROM clientes")
    for row in cursor.fetchall():
        tree_clientes.insert("", "end", values=row)
    conn.close()

 cargar_clientes()

 frame_derecha = Frame(ventana, bg="#ffeaa7")
 frame_derecha.pack(side=RIGHT, fill=Y, padx=10, pady=10)

 etiquetas = ["Nombre", "Apellido", "Teléfono", "Email", "Dirección"]
 entradas = {}
 for etiqueta in etiquetas:
     Label(frame_derecha, text=etiqueta+":", bg="#ffeaa7").pack()
     entrada = Entry(frame_derecha)
     entrada.pack(fill="x", pady=2)
     entradas[etiqueta.lower()] = entrada

 Button(frame_derecha, text="Insertar", command=lambda: insertar_cliente(
     entradas["nombre"], entradas["apellido"], entradas["teléfono"],
     entradas["email"], entradas["dirección"], cargar_clientes), bg="#55efc4").pack(pady=5, fill="x")

 Button(frame_derecha, text="Actualizar", command=lambda: actualizar_cliente(
     tree_clientes, entradas["nombre"], entradas["apellido"], entradas["teléfono"],
     entradas["email"], entradas["dirección"], cargar_clientes), bg="#74b9ff").pack(pady=5, fill="x")

 Button(frame_derecha, text="Eliminar", command=lambda: eliminar_cliente(tree_clientes, cargar_clientes), bg="#ff7675").pack(pady=5, fill="x")

 def cargar_form_cliente(event):
    selected = tree_clientes.selection()
    if selected:
        datos = tree_clientes.item(selected)["values"]
        entradas["nombre"].delete(0, END)
        entradas["nombre"].insert(0, datos[1])
        entradas["apellido"].delete(0, END)
        entradas["apellido"].insert(0, datos[2])
        entradas["teléfono"].delete(0, END)
        entradas["teléfono"].insert(0, datos[3])
        entradas["email"].delete(0, END)
        entradas["email"].insert(0, datos[4])
        entradas["dirección"].delete(0, END)
        entradas["dirección"].insert(0, datos[5])

 tree_clientes.bind("<<TreeviewSelect>>", cargar_form_cliente)

 ventana.mainloop()

if __name__== "__main__":
    mostrar_clientes()