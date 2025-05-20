from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


def mostrar_productos():

    # --- Conexión a la base de datos ---
    def conectar_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Edu@rdo15",
            database="dominos"
        )

    # --- DEF PRODUCTOS ---
    def insertar(nombre, tamano, precio, codigo, refrescar):
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO productos (nombre, tamaño, precio, codigo_barra) VALUES (%s, %s, %s, %s)",
                           (nombre.get(), tamano.get(), precio.get(), codigo.get()))
            conn.commit()
            conn.close()
            refrescar()
            limpiar_campos(nombre, tamano, precio, codigo)
            messagebox.showinfo("Éxito", "Producto insertado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(tree, refrescar):
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")
            return
        id_producto = tree.item(item)["values"][0]
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id_productos=%s", (id_producto,))
            conn.commit()
            conn.close()
            refrescar()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar(tree, nombre, tamano, precio, codigo, refrescar):
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Selecciona un producto para actualizar.")
            return
        try:
            id_producto = tree.item(item)["values"][0]
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("""UPDATE productos 
                              SET nombre=%s, tamaño=%s, precio=%s, codigo_barra=%s 
                              WHERE id_productos=%s""",
                           (nombre.get(), tamano.get(), precio.get(), codigo.get(), id_producto))
            conn.commit()
            conn.close()
            refrescar()
            limpiar_campos(nombre, tamano, precio, codigo)
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_campos(nombre, tamano, precio, codigo):
        nombre.delete(0, END)
        tamano.delete(0, END)
        precio.delete(0, END)
        codigo.delete(0, END)

    # --- VENTANA PRINCIPAL ---
    ventana = Tk()
    ventana.title("Gestión de Productos - Dominos Pizza")
    ventana.geometry("950x600")
    ventana.minsize(800, 500)

    ventana.columnconfigure(0, weight=3)
    ventana.columnconfigure(1, weight=1)
    ventana.rowconfigure(0, weight=1)

    # Panel izquierdo
    izquierda = Frame(ventana)
    izquierda.grid(row=0, column=0, sticky="nsew")

    tree = ttk.Treeview(izquierda, columns=("ID", "Nombre", "Tamaño", "Precio", "Código"), show="headings", height=20)
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    def cargar_datos():
        for row in tree.get_children():
            tree.delete(row)
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id_productos, nombre, tamaño, precio, codigo_barra FROM productos")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    cargar_datos()

    # Panel derecho 
    derecha = Frame(ventana, bg="#dfe6e9")
    derecha.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Formulario SIEMPRE visible
    formulario = Frame(derecha, bg="#dfe6e9")
    formulario.pack(pady=10, fill="x")

    Label(formulario, text="Nombre:", bg="#dfe6e9").pack()
    entry_nombre = Entry(formulario)
    entry_nombre.pack(fill="x")

    Label(formulario, text="Tamaño:", bg="#dfe6e9").pack()
    entry_tamano = Entry(formulario)
    entry_tamano.pack(fill="x")

    Label(formulario, text="Precio:", bg="#dfe6e9").pack()
    entry_precio = Entry(formulario)
    entry_precio.pack(fill="x")

    Label(formulario, text="Código de barra:", bg="#dfe6e9").pack()
    entry_codigo = Entry(formulario)
    entry_codigo.pack(fill="x")

    # Botones
    Button(derecha, text="Insertar", command=lambda: insertar(entry_nombre, entry_tamano, entry_precio, entry_codigo, cargar_datos), bg="#81ecec").pack(pady=5, fill="x")
    Button(derecha, text="Actualizar", command=lambda: actualizar(tree, entry_nombre, entry_tamano, entry_precio, entry_codigo, cargar_datos), bg="#74b9ff").pack(pady=5, fill="x")
    Button(derecha, text="Eliminar", command=lambda: eliminar(tree, cargar_datos), bg="#ff7675").pack(pady=5, fill="x")

    def cargar_en_formulario(event):
        selected = tree.selection()
        if selected:
            datos = tree.item(selected)["values"]
            entry_nombre.delete(0, END)
            entry_nombre.insert(0, datos[1])
            entry_tamano.delete(0, END)
            entry_tamano.insert(0, datos[2])
            entry_precio.delete(0, END)
            entry_precio.insert(0, datos[3])
            entry_codigo.delete(0, END)
            entry_codigo.insert(0, datos[4])

    tree.bind("<<TreeviewSelect>>", cargar_en_formulario)

    ventana.mainloop()

if __name__ == "__main__":
    mostrar_productos()
