

class Scannner(object):
    """
    Scanner class for nmap
    """
    def __init__(self, ip: str, port: int, **kwargs):
        self.ip = ip
        self.port = port
        self.creds = kwargs
        