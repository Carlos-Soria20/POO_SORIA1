import tkinter as tk  # Importo la biblioteca tkinter para crear la interfaz gráfica

# Creo la ventana principal de la aplicación
root = tk.Tk()
root.title("Lista de Tareas")  # Le doy un título a la ventana
root.geometry("400x400")       # Establezco el tamaño de la ventana

# Inicializo una lista vacía donde voy a guardar las tareas
tareas = []

# Defino la función para agregar tareas
def agregar_tarea(event=None):
    texto = entrada.get().strip()  # Obtengo el texto del campo de entrada y elimino espacios
    if texto:  # Verifico que no esté vacío
        lista.insert(tk.END, texto)  # Agrego el texto a la lista visual
        tareas.append({"texto": texto, "completada": False})  # Guardo la tarea en la lista interna
        entrada.delete(0, tk.END)  # Limpio el campo de entrada

# Defino la función para marcar una tarea como completada
def marcar_completada(event=None):
    seleccion = lista.curselection()  # Verifico qué tarea está seleccionada
    if seleccion:
        index = seleccion[0]
        tarea = tareas[index]
        if not tarea["completada"]:  # Solo la marco si no está ya completada
            tarea["completada"] = True
            lista.delete(index)  # Elimino la tarea original
            lista.insert(index, f"[✔] {tarea['texto']}")  # Inserto la versión marcada
            lista.itemconfig(index, {'fg': 'gray'})  # Cambio el color para indicar que está hecha

# Defino la función para eliminar una tarea
def eliminar_tarea(event=None):
    seleccion = lista.curselection()  # Verifico qué tarea está seleccionada
    if seleccion:
        index = seleccion[0]
        lista.delete(index)  # La elimino de la lista visual
        tareas.pop(index)    # También la elimino de la lista interna

# Defino la función para cerrar la aplicación
def cerrar_app(event=None):
    root.destroy()  # Cierro la ventana principal

# Creo el campo de entrada para escribir nuevas tareas
entrada = tk.Entry(root, width=40)
entrada.pack(pady=10)
entrada.bind("<Return>", agregar_tarea)  # Permito agregar tareas presionando Enter

# Organizo los botones en un frame para que estén alineados
frame_botones = tk.Frame(root)
frame_botones.pack()

# Botón para agregar tareas
btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

# Botón para marcar tareas como completadas
btn_completar = tk.Button(frame_botones, text="Completar", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

# Botón para eliminar tareas
btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Creo la lista visual donde se mostrarán las tareas
lista = tk.Listbox(root, width=50, height=15)
lista.pack(pady=10)

# Asigno atajos de teclado para facilitar el uso
root.bind("<c>", marcar_completada)
root.bind("<C>", marcar_completada)
root.bind("<d>", eliminar_tarea)
root.bind("<D>", eliminar_tarea)
root.bind("<Escape>", cerrar_app)

# Inicio el bucle principal de la aplicación
root.mainloop()

