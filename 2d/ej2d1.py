"""
Enunciado:
Desarrolla una aplicación web básica con Flask que muestre el uso del sistema de registro (logging).

En el desarrollo web es fundamental tener un buen sistema de registro de eventos,
que permita hacer seguimiento de lo que ocurre en nuestra aplicación. Flask proporciona
un objeto logger integrado (app.logger) que permite registrar mensajes con diferentes
niveles de importancia.

Tu tarea es implementar los siguientes endpoints:

1. `GET /info`: Registra un mensaje de nivel INFO y devuelve un mensaje en texto plano.
2. `GET /warning`: Registra un mensaje de nivel WARNING y devuelve un mensaje en texto plano.
3. `GET /error`: Registra un mensaje de nivel ERROR y devuelve un mensaje en texto plano.
4. `GET /critical`: Registra un mensaje de nivel CRITICAL y devuelve un mensaje en texto plano.

Esta actividad te enseñará a utilizar el sistema de registro de Flask,
una habilidad crucial para el desarrollo y depuración de aplicaciones web.
"""

from flask import Flask, jsonify, request, Response

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Configuración básica del logger
    # Por defecto, los mensajes se registrarán en la consola

    @app.route('/info', methods=['GET'])
    def log_info():
        """
        Registra un mensaje de nivel INFO
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel INFO usando app.logger.info()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        log = app.logger.info('Mensaje de nivel INFO')
        return Response(log, mimetype='text/plain')

    @app.route('/warning', methods=['GET'])
    def log_warning():
        """
        Registra un mensaje de nivel WARNING
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel WARNING usando app.logger.warning()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        log = app.logger.warning('Mensaje de nivel WARNING')
        return Response(log, mimetype='text/plain')

    @app.route('/error', methods=['GET'])
    def log_error():
        """
        Registra un mensaje de nivel ERROR
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel ERROR usando app.logger.error()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        log = app.logger.error('Mensaje de nivel ERROR')
        return Response(log, mimetype='text/plain')

    @app.route('/critical', methods=['GET'])
    def log_critical():
        """
        Registra un mensaje de nivel CRITICAL
        """
        # Implementa este endpoint:
        # 1. Registra un mensaje de nivel CRITICAL usando app.logger.critical()
        # 2. Devuelve un mensaje en texto plano indicando que se ha registrado el mensaje
        log = app.logger.critical('Mensaje de nivel CRITICAL')
        return Response(log, mimetype='text/plain')

    @app.route('/status', methods=['GET'])
    def status():
        """
        Endpoint adicional que registra diferentes mensajes según el parámetro de consulta 'level'
        Ejemplo: /status?level=warning
        """
        # Este endpoint es opcional, puedes implementarlo si quieres practicar
        # con parámetros de consulta y logging condicional
        # Obtenemos el valor del parámetro 'level'
        level = request.args.get('level', 'info')

        if level:
            log = app.logger.level(f'This is a {level.upper()} message from status endpoint')
            return f'{level.upper()} message has been logged from status endpoint', 200, {'Content-Type': 'text/plain'}
        return 'Invalid log level', 400, {'Content-Type': 'text/plain'}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
