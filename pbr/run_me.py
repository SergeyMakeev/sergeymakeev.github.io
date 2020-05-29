import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({".js": "application/javascript",})

print("http://localhost:8000")
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()

