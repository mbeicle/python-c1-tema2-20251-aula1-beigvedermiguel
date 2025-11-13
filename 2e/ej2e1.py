"""
Enunciado:
Desarrolla una aplicación web con Flask que demuestre diferentes formas de acceder a la
información enviada en las solicitudes HTTP. Esta aplicación te permitirá entender cómo
procesar diferentes tipos de datos proporcionados por los clientes.

Tu aplicación debe implementar los siguientes endpoints:

1. `GET /headers`: Devuelve los encabezados (headers) de la solicitud en formato JSON.
   - Muestra información como User-Agent, Accept-Language, etc.

2. `GET /browser`: Analiza el encabezado User-Agent y devuelve información sobre:
   - El navegador que está usando el cliente
   - El sistema operativo
   - Si es un dispositivo móvil o no

3. `POST /echo`: Acepta cualquier tipo de datos y devuelve exactamente los mismos datos
   en la misma forma que fueron enviados. Debe manejar:
   - JSON
   - Datos de formulario (form data)
   - Texto plano

4. `POST /validate-id`: Valida un documento de identidad según estas reglas:
   - Debe recibir un JSON con un campo "id_number"
   - El ID debe tener exactamente 9 caracteres
   - Los primeros 8 caracteres deben ser dígitos
   - El último carácter debe ser una letra
   - Devuelve JSON indicando si es válido o no

Esta actividad te enseñará cómo acceder y manipular datos de las solicitudes HTTP,
una habilidad fundamental para crear APIs robustas y aplicaciones web interactivas.
"""

from flask import Flask, jsonify, request
import re

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/headers', methods=['GET'])
    def get_headers():
        """
        Devuelve los encabezados (headers) de la solicitud en formato JSON.
        Convierte el objeto headers de la solicitud en un diccionario.
        """
        # Implementa este endpoint:
        # 1. Accede a los encabezados de la solicitud usando request.headers
        # 2. Convierte los encabezados a un formato adecuado para JSON
        # 3. Devuelve los encabezados como respuesta JSON
        
        # Accedemos a los encabezados como un diccionario
        headers = dict(request.headers)
        # Los devolvemos en formato JSON
        return jsonify(headers)


    @app.route('/browser', methods=['GET'])
    def get_browser_info():
        """
        Analiza el encabezado User-Agent y devuelve información sobre el navegador,
        sistema operativo y si es un dispositivo móvil.
        """
        # Implementa este endpoint:
        # 1. Obtén el encabezado User-Agent de request.headers
        # 2. Analiza la cadena para detectar:
        #    - El nombre del navegador (Chrome, Firefox, Safari, etc.)
        #    - El sistema operativo (Windows, macOS, Android, iOS, etc.)
        #    - Si es un dispositivo móvil (detecta cadenas como "Mobile", "Android", "iPhone")
        # 3. Devuelve la información como respuesta JSON
        
        # Accedemos al encabezado 'User-Agent'
        user_agent = request.headers.get('User-Agent')

        # Localizamos la cadena del navegador
        if re.search(r'Chrome', user_agent):
            browser = "Chrome"
        elif re.search(r'Firefox', user_agent):
            browser = "Firefox"
        elif re.search(r'Safari', user_agent):
            browser = "Safari"
        elif re.search(r'Edge', user_agent):
            browser = "Internet Explorer/Edge"
        
        # El Sist. Operativo
        if re.search(r'Windows', user_agent):
            os = "Windows"
        elif re.search(r'Macintosh', user_agent):
            os = "iOS"
        elif re.search(r'Mac OS', user_agent):
            os = 'iPhone'
        elif re.search(r'Linux', user_agent):
            os = "Linux"
        elif re.search(r'Android', user_agent):
            os = "Android"
        elif re.search(r'iPhone', user_agent):
            os = "iOS"
        
        # Si se trata de un dispositivo móvil
        if re.search(r'Mobi', user_agent) or re.search(r'Android', user_agent) or re.search(r'iPhone', user_agent):
            mobile = True
        else:
            mobile = False
    
        return jsonify({'browser': browser, 'os': os, 'is_mobile': mobile})

    @app.route('/echo', methods=['POST'])
    def echo():
        """
        Devuelve exactamente los mismos datos que recibe.
        Debe detectar el tipo de contenido y procesarlo adecuadamente.
        """
        # Implementa este endpoint:
        # 1. Detecta el tipo de contenido de la solicitud con request.content_type
        # 2. Según el tipo de contenido, extrae los datos:
        #    - Para JSON: usa request.get_json()
        #    - Para form data: usa request.form
        #    - Para texto plano: usa request.data
        # 3. Devuelve los mismos datos con el mismo tipo de contenido
        
        # Averiguamos el tipo de contenido
        contenido = request.content_type
        # Si 'content_type' es JSON
        if 'application/json' in contenido:
            # Recuperamos el cuerpo de la solicitud
            contenido_json = request.get_json()
            return contenido_json

        # Si el contenido es FORM
        elif 'application/x-www-form-urlencoded' in contenido:
            # Recuperamos el cuerpo de la solicitud
            contenido_form = request.form
            return jsonify(contenido_form), 200

        # Si el contenido es TEXTO PLANO
        elif 'text/plain' in contenido:
            # Recuperamos el cuerpo de la solicitud
            contenido_text = request.data
            return contenido_text
        
        return jsonify({'message': 'Content-Type inadecuado'}), 400

    @app.route('/validate-id', methods=['POST'])
    def validate_id():
        """
        Valida un documento de identidad según reglas específicas:
        - Debe tener exactamente 9 caracteres
        - Los primeros 8 caracteres deben ser dígitos
        - El último carácter debe ser una letra
        """
        # Implementa este endpoint:
        # 1. Obtén el campo "id_number" del JSON enviado
        # 2. Valida que cumpla con las reglas especificadas
        # 3. Devuelve un JSON con el resultado de la validación
        
        # Verificamos si la solicitud tiene datos en formato JSON
        if not request.is_json:
            return jsonify({'message' : 'El contenido de la solicitud no es un JSON válido'}), 200
        # Recuperamos el cuerpo de la solicitud
        data = request.get_json()
        if not data or 'id_number' not in data:
            return jsonify({'error': 'La solicitud no contiene el campo ID'}), 400
        # Obtenemos el 'id_number'
        id = data['id_number']
        if len(id) == 9 and id[:8].isdigit() and id[-1].isalpha():
            valid_id = True
            return jsonify({'message': 'ID válido', 'valid': valid_id}), 200
        else:
            valid_id = False
            return jsonify({'message': 'Composición incorrecta del ID', 'valid': valid_id}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
