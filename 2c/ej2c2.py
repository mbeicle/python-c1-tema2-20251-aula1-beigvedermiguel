"""
Enunciado:
Desarrolla una API REST utilizando Flask que permita realizar operaciones básicas sobre una lista de tareas (to-do list).
La API debe exponer los siguientes endpoints:

1. `GET /tasks`: Devuelve la lista completa de tareas.
2. `POST /tasks`: Agrega una nueva tarea. El cuerpo de la solicitud debe incluir un JSON con el campo "name".
3. `DELETE /tasks/<task_id>`: Elimina una tarea específica por su ID.
4. `PUT /tasks/<task_id>`: Actualiza el nombre de una tarea existente por su ID. El cuerpo de la solicitud debe incluir un JSON con el campo "name".

Observa que el mismo endpoint (por ejemplo, `/tasks/<task_id>`) puede recibir diferentes verbos HTTP (DELETE, PUT) y realizar distintas operaciones según el verbo utilizado. Esta es una característica fundamental de las APIs REST.

Requisitos:
- Cada tarea debe tener un ID único (entero) y un nombre (cadena de texto).
- La lista de tareas debe almacenarse en memoria (no es necesario usar una base de datos).
- Maneja errores como intentar eliminar o actualizar una tarea que no existe.

Ejemplo:
Si la lista de tareas inicial está vacía:
1. Una solicitud `POST /tasks` con el cuerpo `{"name": "Comprar leche"}` debe agregar la tarea con ID 1.
2. Una solicitud `GET /tasks` debe devolver `[{"id": 1, "name": "Comprar leche"}]`.
3. Una solicitud `PUT /tasks/1` con el cuerpo `{"name": "Comprar pan"}` debe actualizar la tarea con ID 1.
4. Una solicitud `GET /tasks` debe devolver `[{"id": 1, "name": "Comprar pan"}]`.
5. Una solicitud `DELETE /tasks/1` debe eliminar la tarea con ID 1.
6. Una solicitud `GET /tasks` debe devolver `[]`.

Tu tarea es implementar esta API en Flask.
"""

from flask import Flask, jsonify, request

# Esta lista almacenará todas las tareas
tasks = []
# Este contador se usará para asignar IDs únicos
next_id = 1

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        """
        Devuelve la lista completa de tareas
        """
        # Implementa este endpoint
        return tasks

    @app.route('/tasks', methods=['POST'])
    def add_task():
        """
        Agrega una nueva tarea
        El cuerpo de la solicitud debe incluir un JSON con el campo "name"
        """
        # Implementa este endpoint
        # Obtiene los datos JSON del cuerpo de la petición.
        new_task = {'id': next_id}
        new_task.update(request.get_json())

        # Valida que los datos existan.
        if not new_task:
            return jsonify({'error': 'La solicitud debe contener datos JSON'}), 400

        # Agrega la nueva tarea a la lista 'tasks'.
        tasks.append(new_task)

        # Devuelve la nueva tarea con el código de estado 201.
        return jsonify(tasks[next_id - 1]), 201

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        """
        Elimina una tarea específica por su ID
        """
        # Implementa este endpoint
        # Declaramos tasks como 'global' para poder modificarla
        # puesto que está fuera del alcance de la función.
        global tasks
        
        # Primero comprobamos que el id de la tarea exista
        task = next((task for task in tasks if task['id'] == task_id), None)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        # Si existe, se usa una "list comprehension" para crear una nueva lista
        # que excluya la tarea con el id que queremos eliminar.
        tasks = [task for task in tasks if task['id'] != task_id]

        # Se devuelve una respuesta de éxito con un código 200.
        return jsonify({'message': 'Task deleted'}), 200

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        """
        Actualiza el nombre de una tarea existente por su ID
        El cuerpo de la solicitud debe incluir un JSON con el campo "name"
        Código de estado: 200 - OK si se actualizó, 404 - Not Found si no existe
        """
        # Implementa este endpoint
        # Primero comprobamos que el id de la tarea exista
        task = next((task for task in tasks if task['id'] == task_id), None)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        # Se recuperan los datos de la petición
        datos = request.get_json()
        if not datos:
            return jsonify({'error': 'La solicitud debe contener datos JSON'}), 400

        # Se limpia la tarea y se actualiza con los nuevos datos
        task.clear()
        datos = {'id': next_id, 'name': 'Tarea actualizada'}
        task.update(datos)
        # Se devuelve la tarea actualizada con un código 200.
        return jsonify(task), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)