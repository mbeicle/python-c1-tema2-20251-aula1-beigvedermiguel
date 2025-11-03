"""
Enunciado:
Desarrolla una API REST básica utilizando la biblioteca http.server de Python con un endpoint que devuelve información sobre productos.

Tu tarea es implementar el siguiente endpoint:

`GET /product/<id>`: Devuelve información sobre un producto específico por su ID.
- Si el producto existe, devuelve los datos del producto con código 200 (OK).
- Si el producto no existe, devuelve un mensaje de error con código 404 (Not Found).

Requisitos:
- Utiliza la lista de productos proporcionada.
- Devuelve las respuestas en formato JSON.
- Asegúrate de utilizar los códigos de estado HTTP apropiados.

Ejemplo:
1. Una solicitud `GET /product/1` debe devolver los datos del producto con ID 1 y código 200.
2. Una solicitud `GET /product/999` debe devolver un mensaje de error con código 404.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re

# Lista de productos predefinida
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Tablet", "price": 349.99}
]


class ProductAPIHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP para la API de productos
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.
        Debes implementar la lógica para responder a la petición GET en la ruta /product/<id>
        con los datos del producto en formato JSON si existe, o un error 404 si no existe.
        """
        # Implementa aquí la lógica para responder a las peticiones GET
        # 1. Usa una expresión regular para verificar si la ruta coincide con /product/<id>
        # 2. Si coincide, extrae el ID del producto de la ruta
        # 3. Busca el producto en la lista
        # 4. Si el producto existe, devuélvelo en formato JSON con código 200
        # 5. Si el producto no existe, devuelve un mensaje de error con código 404

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
            for product in products:
                if int(id) == product['id']:
                    # Configuramos la respuesta
                    self.send_response(200)  # Código HTTP 200 OK
                    self.send_header("Content-type", "application/json")
                    self.end_headers()

                    product_info = {
                        "id": product['id'],
                        "name": product['name'],
                        "price": product['price']
                    }

                    # Enviamos mensaje
                    self.wfile.write(json.dumps(product_info, indent=4).encode('utf-8'))
                    return
            
            # Si el producto no existe (error 404)
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Producto no encontrado.")
        else:
            # Para otras rutas (error 404)
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Ruta no encontrada. Error 404.")

def create_server(host="localhost", port=8889):
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
