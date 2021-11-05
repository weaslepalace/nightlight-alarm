import socket

class HttpFriend:
    
    _event_handler = {}

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

    def __init__(self):
        pass

    def start_server(self): 
        addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(addr)
        self._sock.listen(1)
        print(f"Listening on {addr}")
    
    def parse_request(self, req):
        print(req)
        line = req.split("\r\n")
        element = line[0].split()
       
        top_line = {
            "method" : element[0],
            "route" : element[1],
            "version" : element[2]
        }

        line = [ln for ln in line if len(ln) == 2]
        headers = {}
        for header in line[1:]:
            h = header.split(":", 1)
            print(h)
            headers[h[0].strip().lower()] = h[1].strip()

        print(headers)

        payload = ""
        if "content-length" in headers:
            #This assumes that there is payload if content-length is provided
            payload = req[:-headers["content-length"]]
        
        parsed_req = {
            "top_line" : top_line,
            "headers" : headers,
            "payload" : payload
        }

        return parsed_req

    def serve(self, router):
        while True:
            client, addr = self._sock.accept()
            print(f"Connection for {addr}")
            req = client.recv(1024)
            if not req or len(req) == 0:
                client.close()

            parsed_req = self.parse_request(req.decode())
            result = router.dispatch(
                parsed_req["top_line"]["route"],
                parsed_req) 

            client.send(self._header(
                result["code"],
                result["mimetype"],
                len(result["contents"])))
            client.send(bytearray(result["contents"].encode()))
            client.close()
