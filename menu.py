from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import clientes, empleados, productos, proveedores, ingredientes

#20 de mayo

#--- Datos de acceso ---
usuarios = "eduardo"
contraseñas = 23270657


def nuevo():
    menu = Tk()
    menu.title("MENÚ PRINCIPAL")
    menu.geometry("400x500")
    menu.configure(bg="#f0f4f8")

    # Título
    titulo = Label(menu, text="Menú Principal", font=("Segoe UI", 18, "bold"), bg="#f0f4f8", fg="#333")
    titulo.pack(pady=20)

    # Frame para botones
    frame_botones = Frame(menu, bg="#f0f4f8")
    frame_botones.pack(pady=10)

    btn_style = {
        "height": 2,
        "width": 18,
        "bg": "#d0e1f9",
        "fg": "#333",
        "font": ("Segoe UI", 11, "bold"),
        "relief": "flat",
        "activebackground": "#a9c7f5",
        "cursor": "hand2",
    }

    bproductos = Button(frame_botones, text="PRODUCTOS", command=productos.mostrar_productos, **btn_style)
    bproductos.grid(row=0, column=0, pady=8)

    bempleados = Button(frame_botones, text="EMPLEADOS", command=empleados.mostrar_empleados, **btn_style)
    bempleados.grid(row=1, column=0, pady=8)

    bclientes = Button(frame_botones, text="CLIENTES", command=clientes.mostrar_clientes, **btn_style)
    bclientes.grid(row=2, column=0, pady=8)

    bproveedores = Button(frame_botones, text="PROVEEDORES", command=proveedores.mostrar_proveedores, **btn_style)
    bproveedores.grid(row=3, column=0, pady=8)

    bingredientes = Button(frame_botones, text="INGREDIENTES", command=ingredientes.mostrar_ingredientes, **btn_style)
    bingredientes.grid(row=4, column=0, pady=8)

    menu.mainloop()


def inicio():
    def verificar_login():
        usuar = usuario1.get()
        contra = contraseña1.get()
        if usuar == usuarios and contra.isdigit() and int(contra) == contraseñas:
            principal.destroy()
            nuevo()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    principal = Tk()
    principal.geometry("500x250")
    principal.title("Login")
    principal.configure(bg="#e6eef7")

    # Lado izquierdo con imagen y fondo claro
    izquierdo = Frame(principal, bg="#4a90e2", width=225, height=250)
    izquierdo.pack(side="left", fill="both")

    try:
        imagen = Image.open("C:/Users/EduardoGv/Documents/python/Topicos/proyecto_dominos/fondo.jpg")
        imagen = imagen.resize((225, 250))
        fondo = ImageTk.PhotoImage(imagen)
        fondo_label = Label(izquierdo, image=fondo)
        fondo_label.image = fondo
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception:
        # Si no carga la imagen, mostrar un color sólido
        izquierdo.configure(bg="#4a90e2")

    # Lado derecho con campos y botones en colores claros
    derecho = Frame(principal, bg="#f0f4f8", width=275, height=250)
    derecho.pack(side="right", fill="both", expand=True)

    Label(derecho, text="Usuario", bg="#f0f4f8", fg="#333", font=("Segoe UI", 12)).place(x=40, y=60)
    usuario1 = Entry(derecho, font=("Segoe UI", 12))
    usuario1.place(x=130, y=60, width=120)

    Label(derecho, text="Contraseña", bg="#f0f4f8", fg="#333", font=("Segoe UI", 12)).place(x=40, y=110)
    contraseña1 = Entry(derecho, show="*", font=("Segoe UI", 12))
    contraseña1.place(x=130, y=110, width=120)

    btn_login = Button(derecho, text="Iniciar Sesión", bg="#4a90e2", fg="white", font=("Segoe UI", 12, "bold"),
                       activebackground="#357ABD", cursor="hand2", command=verificar_login)
    btn_login.place(x=100, y=170, width=130, height=35)

    principal.mainloop()


inicio()
