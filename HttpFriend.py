import socket

class HttpFriend:
    
    _event_handler = {}

    def _header(self, length):
        h = [
            "HTTP/1.1 200 OK\r\n",
            "Content-Type: text/html\r\n",
            "Connection: close\r\n",
            f"Content-Length: {length}\r\n",
            "\r\n"
        ]
        header = bytearray("".join(h).encode())
        print(header)
        return header

    def parse_route(req):
        req.split("\r\n")
        method = req[0]
        route = req[1]
        version = req[2]

    def __init__(self):
        pass

    def start_server(self): 
        addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(addr)
        self._sock.listen(1)
        print(f"Listening on {addr}")
    
    def serve(self):
        while True:
            client, addr = self._sock.accept()
            print(f"Connection for {addr}")
            req = client.recv(1024)
            if req:
                print(str(req))
            with open("index.html") as f:
                html = f.read()
                 
                client.send(self._header(len(html)))
                client.send(bytearray(html.encode()))
            client.close()

    def add_event(callback, route):
        _event_handlers[route] = callback

def hiya()
    print("Hello!")

if __name__ == "__main__":
    http = HttpFriend()
    http.add_event(hiya, "settime")
    http.start_server()
    http.serve()
