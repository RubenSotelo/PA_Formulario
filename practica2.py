from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Interfaz:
    
    def __init__(self):
        self.ventana = Tk() 
        self.ventana.geometry("400x400") 
        self.ventana.title("Programacion Avanzada") 
        self.ventana.config(bg="#00BCD4")
        self.var_genero = IntVar()
        self.definirEstilo()        
        self.crearElementos()
        self.cargarCampos()
        self.ventana.mainloop()

    def crearElementos(self):
        self.lbNombre = ttk.Label(text="Nombre")
        self.tbNombre = ttk.Entry()
        self.lbApellido = ttk.Label(text="Apellido")
        self.tbApellido = ttk.Entry()
        self.lbTelefono = ttk.Label(text="Telefono")
        self.tbTelefono = ttk.Entry()
        self.lbEdad = ttk.Label(text="Edad")
        self.tbEdad = ttk.Entry()
        self.lbEstatura = ttk.Label(text="Estatura")
        self.tbEstatura = ttk.Entry()
        self.lbGenero = ttk.Label(text="Genero")
        self.rbHombre= ttk.Radiobutton(text="Hombre", variable= self.var_genero, value=1)
        self.rbMujer= ttk.Radiobutton(text="Mujer", variable= self.var_genero, value=2)
        self.btnGuardar = ttk.Button(text='Guardar', command = self.guardar)
        self.btnBorrar = ttk.Button(self.ventana, text='Limpiar', command = self.limpiarCampos)
        
        
    def cargarCampos(self):
        self.lbNombre.pack()
        self.tbNombre.pack()
        self.lbApellido.pack()
        self.tbApellido.pack()
        self.lbTelefono.pack()
        self.tbTelefono.pack()
        self.lbEdad.pack()
        self.tbEdad.pack()
        self.lbEstatura.pack()
        self.tbEstatura.pack()
        self.lbGenero.pack()
        self.rbHombre.pack()
        self.rbMujer.pack()
        self.btnGuardar.pack()
        self.btnBorrar.pack()
        
    def definirEstilo(self):
        estilo = ttk.Style(self.ventana)
        estilo.configure("TButton", foreground = "#000000", background ="#00BCD4", pady=15)
        estilo.configure("TLabel", foreground = "#000000", background ="#00BCD4")
        estilo.configure("TEntry", foreground = "#000000", background ="#00BCD4")
        estilo.configure("TRadiobutton", foreground = "#000000", background ="#00BCD4")
        
    def limpiarCampos(self):
        self.tbNombre.delete(0, END)
        self.tbApellido.delete(0, END)
        self.tbEdad.delete(0, END)
        self.tbTelefono.delete(0, END)
        self.tbEstatura.delete(0, END)
        self.var_genero.set(0)
        
    def guardar(self):
        genero = ''
        nombre = self.tbNombre.get()
        apellido = self.tbApellido.get()
        edad = self.tbEdad.get()
        telefono = self.tbTelefono.get()
        estatura = self.tbEstatura.get()
        genero = "Hombre" if self.var_genero.get() == 1 else "Mujer"
        datos = "Nombre: "+nombre+"\n"+"Apellido: "+apellido+"\n"+"Edad: "+edad+"\n"+"Telefono: "+telefono+"\n"+"Estatura: "+estatura+"\n""Genero: "+genero+"\n"
        with open("tarea.txt", "a") as archivo:
            archivo.write(datos+"\n\n")
        messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n"+datos)
        self.limpiarCampos()
        
Interfaz()