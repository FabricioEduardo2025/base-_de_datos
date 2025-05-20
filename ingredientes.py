from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def mostrar_ingredientes():
    
 def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Edu@rdo15",
        database="dominos"
    )

 def insertar_ingrediente(nombre, stock, unidad, refrescar):
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ingredientes (nombre, stock, unidad)
            VALUES (%s, %s, %s)
        """, (nombre.get(), float(stock.get()), unidad.get()))
        conn.commit()
        conn.close()
        refrescar()
        limpiar_formulario(nombre, stock, unidad)
        messagebox.showinfo("Éxito", "Ingrediente insertado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 def eliminar_ingrediente(tree, refrescar):
    item = tree.selection()
    if not item:
        messagebox.showwarning("Advertencia", "Selecciona un ingrediente para eliminar.")
        return
    id_ing = tree.item(item)["values"][0]
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ingredientes WHERE id_ingrediente=%s", (id_ing,))
        conn.commit()
        conn.close()
        refrescar()
        messagebox.showinfo("Éxito", "Ingrediente eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 def actualizar_ingrediente(tree, nombre, stock, unidad, refrescar):
    item = tree.selection()
    if not item:
        messagebox.showwarning("Advertencia", "Selecciona un ingrediente para actualizar.")
        return
    id_ingrediente = tree.item(item)["values"][0]
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE ingredientes
            SET nombre=%s, stock=%s, unidad=%s
            WHERE id_ingrediente=%s
        """, (nombre.get(), float(stock.get()), unidad.get(), id_ingrediente))
        conn.commit()
        conn.close()
        refrescar()
        limpiar_formulario(nombre, stock, unidad)
        messagebox.showinfo("Éxito", "Ingrediente actualizado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 def limpiar_formulario(nombre, stock, unidad):
    for campo in [nombre, stock, unidad]:
        campo.delete(0, END)

 # --- Interfaz ---
 ventana = Tk()
 ventana.title("Gestión de Ingredientes")
 ventana.geometry("800x500")

 frame_izquierda = Frame(ventana)
 frame_izquierda.pack(side=LEFT, fill=BOTH, expand=True)

 tree_ing = ttk.Treeview(frame_izquierda, columns=("ID", "Nombre", "Stock", "Unidad"), show="headings")
 for col in tree_ing["columns"]:
    tree_ing.heading(col, text=col)
    tree_ing.column(col, width=100)
 tree_ing.pack(fill=BOTH, expand=True, padx=10, pady=10)

 def cargar_ingredientes():
    for row in tree_ing.get_children():
        tree_ing.delete(row)
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id_ingrediente, nombre, stock, unidad FROM ingredientes")
    for row in cursor.fetchall():
        tree_ing.insert("", "end", values=row)
    conn.close()

 cargar_ingredientes()

 frame_derecha = Frame(ventana, bg="#dfe6e9")
 frame_derecha.pack(side=RIGHT, fill=Y, padx=10, pady=10)

 Label(frame_derecha, text="Nombre:", bg="#dfe6e9").pack()
 nombre_ing = Entry(frame_derecha)
 nombre_ing.pack(fill="x", pady=2)

 Label(frame_derecha, text="Stock:", bg="#dfe6e9").pack()
 stock_ing = Entry(frame_derecha)
 stock_ing.pack(fill="x", pady=2)

 Label(frame_derecha, text="Unidad:", bg="#dfe6e9").pack()
 unidad_ing = Entry(frame_derecha)
 unidad_ing.pack(fill="x", pady=2)

 Button(frame_derecha, text="Insertar", command=lambda: insertar_ingrediente(
     nombre_ing, stock_ing, unidad_ing, cargar_ingredientes), bg="#55efc4").pack(pady=5, fill="x")

 Button(frame_derecha, text="Actualizar", command=lambda: actualizar_ingrediente(
     tree_ing, nombre_ing, stock_ing, unidad_ing, cargar_ingredientes), bg="#74b9ff").pack(pady=5, fill="x")

 Button(frame_derecha, text="Eliminar", command=lambda: eliminar_ingrediente(tree_ing, cargar_ingredientes), bg="#ff7675").pack(pady=5, fill="x")

 def cargar_form(event):
    selected = tree_ing.selection()
    if selected:
        datos = tree_ing.item(selected)["values"]
        nombre_ing.delete(0, END)
        nombre_ing.insert(0, datos[1])
        stock_ing.delete(0, END)
        stock_ing.insert(0, datos[2])
        unidad_ing.delete(0, END)
        unidad_ing.insert(0, datos[3])

 tree_ing.bind("<<TreeviewSelect>>", cargar_form)

 ventana.mainloop()

if __name__== "__main__":
    mostrar_ingredientes()
    

#20 de mayo