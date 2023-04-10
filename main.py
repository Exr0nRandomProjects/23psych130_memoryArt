

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
    image_to_send = get_image()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        #self.wfile.write(bytes("utterly based", 'utf-8'))
        #self.wfile.write(get_image())
        self.wfile.write(bytes(big_string.format(imgdata=self.image_to_send.decode('utf-8')), 'utf-8'))
        self.image_to_send = get_image() # send the image from the previous iteration

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


