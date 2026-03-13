"""
Esta clase manipula los datos.
"""
from model.task import Task
from uuid import UUID

class TaskRepository:
    _task: list[Task] = [
        Task("Leer un libro", "Debo leer el libro 'El diario de Ana Frank'"),
        Task("Practica programación", "Debo practica mucho Python."),
        Task("Ver anime", "Debo dedicar solo media hora para Dragon Ball Z")
    ]

    def get_all(self) -> list[Task]:
        return self._task

    def delete_one(self, uuid: UUID) -> None:
        print("Eliminado tarea: ", uuid)
