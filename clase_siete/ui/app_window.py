import tkinter as tk
from tkinter import ttk
from service.task_service import TaskService


class AppWindow(tk.Tk):

    def __init__(self, task_service: TaskService) -> None:
        super().__init__()
        self._task_service = task_service

        self.title("Tkinter desde POO")
        self.geometry("500x500")
        self.resizable(False, False)

        # Crear interfaz
        self.create_widgets()

        # Cargar datos en la tabla
        tasks = self._task_service.get_all_task()

        for task in tasks:
            self.tree.insert("", "end", values=(task.uuid, task.title, task.description))

    def create_widgets(self) -> None:
        label = tk.Label(self, text="Bienvenido a mi App")
        label.pack()

        # Input para título
        self.title_label = tk.Label(self, text="Titulo")
        self.title_label.pack()

        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        # Input para descripción
        self.description_label = tk.Label(self, text="Descripcion")
        self.description_label.pack()

        self.description_entry = tk.Entry(self)
        self.description_entry.pack()

        # Botón
        self.create_button = tk.Button(self, text="Guardar", command=self.create_task)
        self.create_button.pack()

        # Tabla
        self.tree = ttk.Treeview(
            self,
            columns=("uuid", "title", "description"),
            show="headings"
        )

        self.tree.heading("uuid", text="ID")
        self.tree.heading("title", text="Titulo")
        self.tree.heading("description", text="Descripcion")

        self.tree.pack(fill="both", expand=True)

    def create_task(self):
        titulo = self.title_entry.get()
        descripcion = self.description_entry.get()

        self._task_service.create_task(titulo, descripcion)

        # Limpiar inputs
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Volver a cargar datos
        tasks = self._task_service.get_all_task()

        for task in tasks:
            self.tree.insert("", "end", values=(task.uuid, task.title, task.description))