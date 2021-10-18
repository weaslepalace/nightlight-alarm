import network

class AccessPointFriend:

    def __init__(self, ssid, max_conns):
        self._ssid = ssid
        self._max_connections = max_conns

    def start(self):
        self._ap = network.WLAN(network.AP_IF)
        self._ap.config(essid=self._ssid)
        self._ap.config(max_clients=self._max_connections)
        self._ap.active(True)
    
