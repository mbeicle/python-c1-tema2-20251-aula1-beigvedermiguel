"""
Enunciado:
Desarrolla una aplicación web con Flask que utilice la función abort() para devolver
diferentes códigos de estado HTTP según ciertas condiciones.

La función abort() de Flask permite terminar prematuramente una solicitud con un código
de estado HTTP específico. Esto es útil para indicar errores como recurso no encontrado (404),
acceso prohibido (403), etc.

Tu tarea es implementar los siguientes endpoints:

1. `GET /resource/<id>`: Debe devolver un mensaje con el ID solicitado si el ID es un número positivo.
   Si el ID es 0 o negativo, debe abortar la solicitud con código 400 (Bad Request).
   Si el ID es mayor que 100, debe abortar la solicitud con código 404 (Not Found).

2. `GET /admin`: Debe verificar si existe un parámetro de consulta 'key'.
   Si 'key' no está presente, debe abortar la solicitud con código 401 (Unauthorized).
   Si 'key' no es igual a 'secret123', debe abortar la solicitud con código 403 (Forbidden).

Esta actividad te enseñará a utilizar la función abort() de Flask para manejar
situaciones de error comunes en aplicaciones web.
"""

from flask import Flask, request, abort, jsonify

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/resource/<resource_id>', methods=['GET'])
    def get_resource(resource_id):
        """
        Devuelve información sobre un recurso según su ID.
        Utiliza abort() en casos de error:
        - Si el ID es <= 0: abort con código 400 (Bad Request)
        - Si el ID es > 100: abort con código 404 (Not Found)
        """
        # Implementa este endpoint utilizando abort() según las condiciones
        # Comprobamos si se ha introducido el 'resource_id
        if not resource_id:
            return jsonify({'message': 'Debe proporcionar un recurso'})
        # Recuperamos el dato y lo convertimos a 'int'
        resource_id = int(resource_id)
        # Tratamos los códigos
        if resource_id <= 0:
            abort(400)                  # Bad Request
        elif resource_id > 100:
            abort(404)                  # Not Found

        return jsonify({'message': f'Se ha accedido al recurso: {resource_id}'}), 200


    @app.route('/admin', methods=['GET'])
    def admin():
        """
        Endpoint protegido que requiere una clave de acceso.
        Utiliza abort() en casos de error:
        - Si no se proporciona el parámetro 'key': abort con código 401 (Unauthorized)
        - Si la clave no es 'secret123': abort con código 403 (Forbidden)
        """
        # Implementa este endpoint utilizando abort() según las condiciones
        # Se recupera el 'key'
        key = request.args.get('key')
        # Si no se ha introducido
        if not key:
            abort(401)          # Unauthorized
        # Si el key es erróneo
        if key != 'secret123':
            abort(403)          # Forbidden

        return jsonify({'message': 'Acceso permitido.'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
