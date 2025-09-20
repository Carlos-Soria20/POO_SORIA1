# Importo los módulos necesarios para crear la interfaz gráfica
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Uso este widget para facilitar la selección de fechas

# Defino la clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):  # Inicializo la interfaz y todos sus componentes
        self.root = root
        self.root.title("Agenda Personal")  # Le doy un título a la ventana
        self.root.geometry("600x400")       # Establezco el tamaño inicial

        #  Frame para TreeView (lista de eventos)
        frame_lista = ttk.Frame(root)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Creo el TreeView para mostrar los eventos con columnas personalizadas
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha") # Encabezado para la columna de fecha
        self.tree.heading("Hora", text="Hora") # Encabezado para la columna de hora
        self.tree.heading("Descripción", text="Descripción") # Encabezado para la columna de descripción
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        frame_entrada = ttk.Frame(root) # Marco para los campos de entrada
        frame_entrada.pack(fill=tk.X, padx=10, pady=5)

        # Agrego los campos de entrada para fecha, hora y descripción
        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=2)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')  # Formato de fecha estándar
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=2)
        # Etiqueta y campo para la hora
        ttk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=2)
        self.hora_entry = ttk.Entry(frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=2)
        # Etiqueta y campo para la descripción del evento
        ttk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=2)
        self.desc_entry = ttk.Entry(frame_entrada, width=25)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=2)

        # Frame para botones
        frame_botones = ttk.Frame(root)  # Marco para los botones
        frame_botones.pack(fill=tk.X, padx=10, pady=10)

        # Botón para agregar eventos
        self.btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar eventos seleccionados
        self.btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para cerrar la aplicación
        self.btn_salir = ttk.Button(frame_botones, text="Salir", command=root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=5)

    # Función para agregar un evento a la lista
    def agregar_evento(self):
        fecha = self.fecha_entry.get() # Obtengo la fecha ingresada
        hora = self.hora_entry.get()# Obtengo la hora ingresada
        desc = self.desc_entry.get() # Obtengo la descripción ingresada
        # Verifico que todos los campos estén llenos
        if not (fecha and hora and desc):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return
        # Inserto el evento en el TreeView
        self.tree.insert("", tk.END, values=(fecha, hora, desc))
        # Limpio los campos de hora y descripción para facilitar la entrada de nuevos datos
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    # Función para eliminar el evento seleccionado
    def eliminar_evento(self):
        seleccionado = self.tree.selection() # Obtengo el ítem seleccionado
        # Verifico que haya un evento seleccionado
        if not seleccionado:
            messagebox.showinfo("Selecciona un evento", "Debes seleccionar un evento para eliminarlo.")
            return
        # Pido confirmación antes de eliminar
        if messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el evento seleccionado?"):
            self.tree.delete(seleccionado)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Creo la ventana principal
    app = AgendaApp(root)
    root.mainloop() # Inicio el bucle principal de la interfaz