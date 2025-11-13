"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a diferentes peticiones GET.
La aplicación debe tener los siguientes endpoints:

1. `GET /hello`: Devuelve un mensaje de saludo en texto plano con el contenido "¡Hola mundo!".
2. `GET /goodbye`: Devuelve un mensaje de despedida en texto plano con el contenido "¡Adiós mundo!".
3. `GET /greet/<nombre>`: Devuelve un mensaje personalizado en texto plano con el contenido "¡Hola, <nombre>!", donde <nombre> es un parámetro dinámico.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados.

Nota: Si deseas cambiar el idioma del ejercicio, edita el archivo de prueba correspondiente.
"""

from flask import Flask

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Aquí debes implementar los endpoints solicitados

    # endpoint 'saludo'
    @app.route('/hello', methods=['GET'])
    def saludo():
        # La función devuelve el texto que se mostrará en el navegador.
        return '¡Hola mundo!', 200, {'Content-Type': 'text/plain; charset=utf-8'}

    # endpoint 'adiós'
    @app.route('/goodbye', methods=['GET'])
    def despedida():
        # La función devuelve el texto que se mostrará en el navegador.
        return '¡Adiós mundo!', 200, {'Content-Type': 'text/plain; charset=utf-8'}

    # endpoint 'greet'
    @app.route('/greet/<nombre>', methods=['GET'])
    def saludo_nombre(nombre):
        # La función devuelve el texto que se mostrará en el navegador.
        return f'¡Hola, {nombre}!', 200, {'Content-Type': 'text/plain; charset=utf-8'}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)