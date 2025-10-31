"""
Enunciado:
Desarrolla una API REST básica utilizando la biblioteca http.server de Python con un endpoint que devuelve información sobre productos en formato XML.

Tu tarea es implementar el siguiente endpoint:

`GET /product/<id>`: Devuelve información sobre un producto específico por su ID.
- Si el producto existe, devuelve los datos del producto en formato XML con código 200 (OK).
- Si el producto no existe, devuelve un mensaje de error con código 404 (Not Found).

Requisitos:
- Utiliza la lista de productos proporcionada.
- Devuelve las respuestas en formato XML.
- Asegúrate de utilizar los códigos de estado HTTP apropiados.

Ejemplo:
1. Una solicitud `GET /product/1` debe devolver los datos del producto con ID 1 en formato XML y código 200.
2. Una solicitud `GET /product/999` debe devolver un mensaje de error con código 404.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Lista de productos predefinida
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Tablet", "price": 349.99}
]

def dict_to_xml(tag, d):
    """
    Convierte un diccionario en un elemento XML
    """
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.SubElement(elem, key)
        child.text = str(val)
    return elem

def prettify(elem):
    """
    Devuelve una cadena XML formateada bonita
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ").encode()

class ProductAPIHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP para la API de productos en XML
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.
        Debes implementar la lógica para responder a la petición GET en la ruta /product/<id>
        con los datos del producto en formato XML si existe, o un error 404 si no existe.
        """
        # Implementa aquí la lógica para responder a las peticiones GET
        # 1. Usa una expresión regular para verificar si la ruta coincide con /product/<id>
        # 2. Si coincide, extrae el ID del producto de la ruta
        # 3. Busca el producto en la lista
        # 4. Si el producto existe:
        #    a. Convierte el producto a XML usando dict_to_xml y prettify
        #    b. Devuelve el XML con código 200 y Content-Type application/xml
        # 5. Si el producto no existe, devuelve un mensaje de error XML con código 404
        def busca_prod(self):
            id_str = re.search(r'\d+', self.path)
            if id_str != None:
                return id_str.group(0)
            else:
                return

        id = busca_prod(self)
        if id != None:
            ruta = '/product/' + id
        else:
            ruta = ''
        if self.path == ruta:
            if int(id) <= 3:
                for product in products:
                    if int(id) == product['id']:
                        # Configuramos la respuesta
                        self.send_response(200)  # Código HTTP 200 OK
                        self.send_header("Content-type", "application/xml")
                        self.end_headers()
                        # creamos el diccionario con los datos del producto solicitado
                        product_info = {
                            'id': product['id'],
                            'name': product['name'],
                            'price': product['price']
                        }
                        # Creamos el elemento raíz y convertimos el diccionario
                        elem = dict_to_xml('product', product_info)
                        product_xml = prettify(elem)

                        # Enviamos mensaje
                        self.wfile.write(product_xml)
            else:
                # Si el producto no existe (error 404)
                self.send_response(404)
                self.send_header("Content-Type", "application/xml")
                self.end_headers()
                # creamos el diccionario con el mensaje de error
                product_error = {
                        'code': '404',
                        'error': 'Product not found'
                    }
                # Creamos el elemento raíz y convertimos el diccionario
                elem = dict_to_xml('error', product_error)
                product_error_xml = prettify(elem)
                # Enviamos mensaje
                self.wfile.write(product_error_xml)
        else:
            # Para otras rutas (error 404)
            self.send_response(404)
            self.send_header("Content-Type", "application/xml")
            self.end_headers()
            # creamos el diccionario con el mensaje de error
            route_error = {
                    'code': '404',
                    'error': 'Not found'
                }
            # Creamos el elemento raíz y convertimos el diccionario
            elem = dict_to_xml('error', route_error)
            route_error_xml = prettify(elem)
            # Enviamos mensaje
            self.wfile.write(route_error_xml)

def create_server(host="localhost", port=8890):
    """
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, ProductAPIHandler)
    return httpd

def run_server(server):
    """
    Inicia el servidor HTTP
    """
    print(f"Servidor iniciado en http://{server.server_address[0]}:{server.server_port}")
    try:
        server.serve_forever()
    except:
        print('Servidor detenido por el usuario.')
        server.server_close()

if __name__ == '__main__':
    server = create_server()
    run_server(server)
