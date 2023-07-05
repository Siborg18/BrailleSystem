import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


def run_http_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', PORT)
    httpd = server_class(server_address, handler_class)
    print("serving at port", PORT)
    httpd.serve_forever()
