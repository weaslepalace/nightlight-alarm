import socket
import sys

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

    def stop_server(self):
        self._sock.shutdown(socket.SHUT_RDWR)
        print("Closing socket");
        
    def start_server(self): 
        addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind(addr)
        self._sock.listen(1)
        print(f"Listening on {addr}")

    def parse_request(self, req):
        r = req.split("\r\n\r\n", 1)
        content = r[1]
        line = r[0].split("\r\n")

        element = line[0].split()
       
        top_line = {
            "method" : element[0],
            "route" : element[1],
            "version" : element[2]
        }

        header = [
            ln.split(":", 1)
            for ln in line
            if len(ln.split(":",1)) == 2
        ]
        headers = {}
        for h in header:
            headers[h[0].strip().lower()] = h[1].strip()

        print("Headers:")
        print(headers)

        payload = ""
        if "content-length" in headers:
            #This assumes that there is payload if content-length is provided
            content_length = int(headers["content-length"])
            payload = content[:content_length]
        print("Payload:")
        print(payload)       
 
        parsed_req = {
            "top_line" : top_line,
            "headers" : headers,
            "payload" : payload
        }

        return parsed_req

    def serve(self, router):
        while True:
            try:
                client, addr = self._sock.accept()
            except OSError as e:
                print(e)
                continue

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
