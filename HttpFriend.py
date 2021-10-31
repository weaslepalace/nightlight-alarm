import socket

class HttpFriend:
    
    _event_handler = {}

    class Document:
        def __init__(self, name, mimetype, code):
            self.name = name
            self.mimetype = mimetype
            self.code = code

    index = Document("index.html", "text/html", 200)
    get_datetime = Document("get_local_datetime.js", "text/javascript", 200)
    not_found = Document("not_found.html", "text/html", 404)

    def _header(self, code, content_type, length):
        h = [
            f"HTTP/1.1 {code} OK\r\n",
            f"Content-Type: {content_type}\r\n",
            "Connection: close\r\n",
            f"Content-Length: {length}\r\n",
            "\r\n"
        ]
        header = bytearray("".join(h).encode())
        print(header)
        return header

    def parse_request(self, req):
        print(req)
        line = req.split("\r\n")
        element = line[0].split()
        method = element[0]
        route = element[1]
        version = element[2]
        return method, route, version

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
            if not req or len(req) == 0:
                client.close()

            _, route, _ = self.parse_request(str(req))
 
            doc = (
                self.index if route == "/" else
                self.get_datetime if route == "/get_local_time.js" else
                self.not_found
            )
            
            print(f"Serving {route} with {doc.name} as {doc.mimetype}")
            
            with open(doc.name) as f:
                contents = f.read()
                 
                client.send(self._header(doc.code, doc.mimetype, len(contents)))
                client.send(bytearray(contents.encode()))
            client.close()

    def add_event(callback, route):
        _event_handlers[route] = callback

def hiya():
    print("Hello!")

if __name__ == "__main__":
    http = HttpFriend()
    http.add_event(hiya, "settime")
    http.start_server()
    http.serve()
