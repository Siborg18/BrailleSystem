from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import socket
import socketserver

PORT = 8000


class MyTCPServer(socketserver.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


Handler = SimpleHTTPRequestHandler
httpd = MyTCPServer(("", PORT), Handler)

httpd.serve_forever()



httpd.shutdown()  # If you want to programmatically shut off the server
