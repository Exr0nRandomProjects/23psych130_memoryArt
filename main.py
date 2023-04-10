

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from camera import get_image, cleanup

hostname = ''
port = 8080


big_string = '''
<html>
<head>
<style>
body {{
    background-image: url("data:image/png;base64,{imgdata}");
    background-repeat: no-repeat;
    background-size: cover;
}}
</style>
</head>
<body></body>
</html>
'''

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        #self.wfile.write(bytes("utterly based", 'utf-8'))
        #self.wfile.write(get_image())
        self.wfile.write(bytes(big_string.format(imgdata=get_image().decode('utf-8')), 'utf-8'))

if __name__ == '__main__':
    ws = HTTPServer((hostname, port), Server)
    print(hostname, port)

    try:
        ws.serve_forever()
    except KeyboardInterrupt:
        print("keyboard inturrupt")
    finally:
        ws.server_close()
        cleanup()
    

